# TikTok Liker Pro

**TikTok Liker Pro** is an automated tool designed to simulate human-like interactions on TikTok by logging in, handling CAPTCHA challenges, extracting commenter profile links from a specified video, and then visiting each profile to like a defined number of videos. This repository contains two versions of the tool:

- **TikTok_Liker_Pro_Solo.py** – Processes a single TikTok video URL provided by the user.
- **TikTok_Liker_Pro_Batch.py** – Processes multiple TikTok video URLs read from a file named `Videos.txt` (each URL on a new line).

> **Disclaimer:**  
> This tool is for educational purposes only. Even if it violates TikTok's Terms of Service, the creator of this code is not responsible for any misuse or consequences. Use this tool at your own risk.

---

## Features

- **Automated Login:**  
  Log in to TikTok using your credentials with human-like delayed typing.

- **CAPTCHA Handling:**  
  Continuously checks for CAPTCHA challenges and pauses execution until you solve them manually.

- **Stealth & Human-like Behavior:**  
  Uses a realistic User-Agent along with additional Chrome options for stealth. Random delays and JavaScript-based clicks are implemented to mimic natural user interactions.

- **Commenter Extraction:**  
  Extracts profile links from the comments section of a given TikTok video.

- **Profile Processing:**  
  Visits each commenter’s profile, clicks on the first video, and likes a defined number of videos.

- **Batch Video Processing:**  
  Processes multiple video URLs from a `Videos.txt` file (one URL per line).

- **Unlike All Given Likes:**  
  If the users you interacted with did not reciprocate the likes, you can run a separate script (provided in another repository) to remove all likes given to them.

- **Colored Terminal Output:**  
  Uses Colorama to provide organized, colorful terminal output for easy monitoring of the process.

---

## Why is the Script Slow?

The script is intentionally slow to ensure TikTok registers the likes properly. Increasing the speed could result in TikTok detecting and blocking the likes, preventing them from being counted.

---

## Requirements

The following Python packages are required:

- selenium
- undetected-chromedriver
- colorama

You can install them using the provided [requirements.txt](requirements.txt):

```plaintext
selenium
undetected-chromedriver
colorama
```

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LeaDer-E/TikTok-Liker-Pro.git
   cd TikTok-Liker-Pro
   ```

2. **(Optional) Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### TikTok_Liker_Pro_Solo.py

1. Run the script:

   ```bash
   python TikTok_Liker_Pro_Solo.py
   ```

2. Enter your TikTok username and password when prompted.
3. Provide the TikTok video URL you wish to process.
4. Input the number of commenters (users) to process and the number of videos to like per user.
5. The script will log in, extract commenter links, and process each profile accordingly.

### TikTok_Liker_Pro_Batch.py

1. Create a file named `Videos.txt` in the repository root with video URLs (one URL per line), for example:

   ```
   https://www.tiktok.com/@akram.ahmedd/video/7482115173273160961
   https://www.tiktok.com/@ojastories_35/video/7478095454954179848
   https://www.tiktok.com/@moh2medzan2ty/video/7482782370681195794
   ```

2. Run the script:

   ```bash
   python TikTok_Liker_Pro_Batch.py
   ```

3. Follow the prompts to input your login credentials and parameters.
4. The script will sequentially process each video URL from `Videos.txt`.

---

## Configuration

### Chrome Options & Stealth Settings

The scripts initialize Chrome with options designed to simulate a real user:

```python
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--incognito")
```

### Human-like Behavior

- **Delayed Input:**  
  Simulates human typing with random delays.
- **JavaScript Clicks:**  
  Uses `execute_script` for natural clicking behavior.
- **CAPTCHA Handling:**  
  The script pauses and waits for manual CAPTCHA resolution if detected.

---

## Important Notes

- **Use Responsibly:**  
  Automating interactions may trigger anti-bot measures on TikTok. Use this tool with caution.
  
- **Maintenance:**  
  TikTok’s website structure may change over time, requiring updates to XPaths and logic.
  
- **Educational Purposes Only:**  
  This tool is provided for educational and testing purposes only. Even if it violates TikTok’s Terms of Service, the creator is not responsible for any misuse or consequences.

---

## License

This project is licensed under the MIT License (if applicable).

---

Enjoy using **TikTok Liker Pro**!

