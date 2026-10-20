# Voice to PDF Item Report Generator
import os
import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# Create Recognizer and Item Storage
r = sr.Recognizer()
items = []

# Define Listen Function using sounddevice + soundfile
def listen():
    samplerate = 16000  # Optimal sample rate for speech recognition
    duration = 5        # Record duration in seconds
    temp_filename = "temp_voice_input.wav"
    
    print("\n--- Listening for 5 seconds... Speak now! ---")
    try:
        # Record audio from default microphone
        my_recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
        sd.wait()  # Wait until the recording finishes
        
        # Save recording to a temporary file
        sf.write(temp_filename, my_recording, samplerate)
        
        # Pass the temporary audio file into SpeechRecognition
        with sr.AudioFile(temp_filename) as source:
            audio = r.record(source)
            
        text = r.recognize_google(audio).strip()
        print(f"Recognized Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google service; {e}")
        return ""
    except Exception as e:
        print(f"Audio system error: {e}")
        return ""
    finally:
        # Clean up the temporary file safely
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

# Keep listening until the user says exit or finish
print("Instructions: Say an item name followed by its price (e.g., 'Laptop 50000'). Say 'exit' to finish.")
while True:
    text = listen()
    if not text:
        continue
    if text.lower() in ['exit', 'finish']:
        break

    # Extract Item name and price
    words = text.split()
    price = ""
    
    # Identify the price number in the spoken text
    for w in words:
        if w.replace('.', '', 1).isdigit():
            price = w
            break
            
    # Clean and extract item name
    item_words = [w for w in words if not w.replace('.', '', 1).isdigit() and w.lower() != 'tk']
    item_name = " ".join(item_words)
    
    # Store item in list
    if price and item_name:
        items.append((item_name, price))
        print(f"Successfully Added -> Item: {item_name} | Price: {price}")
    else:
        print("Could not separate item and price clearly. Please say again!")

# Generate PDF report if items exist
if items:
    pdf = canvas.Canvas("item_price_list.pdf", pagesize=A4)
    width, height = A4

    # Title
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(width / 2, height - 60, "Item and Price List")

    # Table configuration
    x_item = 100
    x_price = 400
    y = height - 120

    # Draw header background bar
    pdf.setFillColor(colors.darkblue)
    pdf.rect(80, y - 10, 430, 30, fill=1, stroke=0)

    # Header labels
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x_item, y, "Item")
    pdf.drawString(x_price, y, "Price")
    
    # Reset text colors for loop data
    pdf.setFillColor(colors.black)
    pdf.setFont("Helvetica", 11)
    y -= 35

    # Print rows
    for item, price in items:
        # Handle page overflow safely
        if y < 50:
            pdf.showPage()
            y = height - 60
            pdf.setFont("Helvetica", 11)
            
        pdf.drawString(x_item, y, item)
        
        # Formats the string safely into a float for visual presentation
        try:
            formatted_price = f"{float(price):,.2f}"
        except ValueError:
            formatted_price = price
            
        pdf.drawRightString(480, y, formatted_price)
        
        # Grid line divider
        pdf.setStrokeColor(colors.lightgrey)
        pdf.setLineWidth(0.5)
        pdf.line(80, y - 8, 480, y - 8)
        y -= 30

    pdf.save()
    print("\n[Success] PDF created: item_price_list.pdf")
else:
    print("\nNo items were added. PDF generation skipped.")