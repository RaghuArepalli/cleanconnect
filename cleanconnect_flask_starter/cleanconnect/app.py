from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    events = [
        {
            "title": "Kukatpally Road Cleanup",
            "location": "Kukatpally, Hyderabad",
            "date": "Sunday, 13 September 2026",
            "time": "7:00 AM - 10:00 AM",
            "volunteers": 32,
            "image": "cleanup1.svg"
        },
        {
            "title": "Durgam Cheruvu Lake Cleanup",
            "location": "Durgam Cheruvu, Hyderabad",
            "date": "Sunday, 20 September 2026",
            "time": "6:30 AM - 10:00 AM",
            "volunteers": 45,
            "image": "cleanup2.svg"
        },
        {
            "title": "KBR Park Cleanup",
            "location": "KBR National Park, Hyderabad",
            "date": "Sunday, 27 September 2026",
            "time": "7:00 AM - 10:00 AM",
            "volunteers": 28,
            "image": "cleanup3.svg"
        }
    ]
    return render_template("index.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)
