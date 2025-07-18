📝 Gemini AI Blog Generator
Welcome to Gemini AI Blog Generator — an AI-powered blogging assistant that helps you generate high-quality, informative blog posts using Google's Gemini 2.5 Pro model. Built with Streamlit, this app allows you to input a topic, select tone and word count, and instantly generate downloadable blog content.

🚀 Features
    ✅ Easy-to-use Streamlit interface
    🎭 Tone selection: Formal, Casual, Creative, Professional
    ✍️ Word limit control: 100 to 1000 words
    📩 Download blog as .txt file
    🌑 Dark mode compatible (via Streamlit settings)
    💬 Gemini 2.5 Pro model for high-quality content generation
    
    
🖥️ Demo

AI-generated blog in seconds

Of course! Here is a casual blog post on the benefits of AI in healthcare.

***

### Your Doctor's New Super-Powered Assistant? It's AI.

Heard the term "AI" and immediately pictured sci-fi robots? When it comes to healthcare, the reality is a lot more practical—and exciting! Think of AI less as a replacement for your doctor and more as a super-powered assistant, working behind the scenes to improve our health.

One of its biggest game-changers is in diagnostics. AI algorithms can analyze medical scans like X-rays and MRIs with incredible precision, often spotting early signs of diseases like cancer or diabetic retinopathy that a human eye might miss. This means catching problems sooner, which is huge for successful treatment.

It’s also making medicine more personal. Instead of a one-size-fits-all approach, AI can help create treatment plans tailored to your specific genetic makeup and lifestyle. It's even speeding up the creation of new drugs by analyzing data at a pace humans never could.

From reducing tedious paperwork so nurses can focus on patients, to powering the health alerts on your smartwatch, AI is a powerful new tool in the medical kit. It’s all about empowering our healthcare heroes and giving us all a better shot at a long, healthy life.



🛠️ Installation
1. Clone the repository
   
bash
git clone https://github.com/Ishwari-Khebade/gemini-blog-generator.git
cd gemini-blog-generator


2. Create and activate a virtual environment (optional but recommended)
bash

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install required packages
bash

pip install -r requirements.txt


▶️ Run the App
bash

streamlit run app.py

📁 Project Structure

gemini-blog-generator/
│
├── app.py              # Streamlit main application
├── requirements.txt    # Python dependencies
├── api.env             # API Key file (optional)
└── README.md           # Project documentation


📌 Notes
Ensure you have access to Gemini Pro 2.5 API on Google AI Studio.

If you're getting 404 errors, make sure the model name is valid and enabled in your project.

For PDF export and images via Gemini Vision or DALL·E, enhancements can be added (coming soon).

📃 License
This project is open-source and available under the MIT License.

👩‍💻 Author
Ishwari Khebade
🔗 GitHub: @Ishwari-Khebade
