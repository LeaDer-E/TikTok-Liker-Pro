import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from colorama import init, Fore, Style

# Initialize Colorama for colored terminal output
init(autoreset=True)

# Set up Chrome options with a realistic User-Agent and additional stealth options
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

print(Fore.MAGENTA + "Initializing Chrome with custom options..." + Style.RESET_ALL)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# ------------------------ Helper Functions ------------------------

def delayed_input(text, element):
    """Simulate human-like delayed typing."""
    for letter in text:
        element.send_keys(letter)
        time.sleep(random.uniform(0.01, 0.1))

def handle_captcha(driver):
    """Pause execution if a CAPTCHA is detected."""
    try:
        captcha_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "captcha-verify-container"))
        )
        if captcha_element:
            print(Fore.RED + "CAPTCHA detected! Please solve it and press Enter to continue..." + Style.RESET_ALL)
            input()
            WebDriverWait(driver, 60).until_not(
                EC.presence_of_element_located((By.CLASS_NAME, "captcha-verify-container"))
            )
            print(Fore.GREEN + "CAPTCHA solved successfully. Continuing..." + Style.RESET_ALL)
    except TimeoutException:
        pass

def login(username, password):
    """Log in to TikTok with provided credentials."""
    try:
        driver.get("https://www.tiktok.com/login")
        time.sleep(2)
        handle_captcha(driver)
        
        # Click "Use phone / email / username"
        use_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/div/div/div/div[3]/div[2]/div[2]/div'))
        )
        use_option.click()
        time.sleep(1)
        handle_captcha(driver)
        print(Fore.CYAN + "Clicked on 'Use phone / email / username'." + Style.RESET_ALL)

        # Click "Login with email or username"
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/a'))
        )
        login_link.click()
        time.sleep(1)
        handle_captcha(driver)
        print(Fore.CYAN + "Clicked on 'Login with email or username'." + Style.RESET_ALL)

        # Enter username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[1]/input'))
        )
        delayed_input(username, username_field)
        print(Fore.GREEN + "Username entered successfully." + Style.RESET_ALL)

        # Enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div/input'))
        )
        delayed_input(password, password_field)
        print(Fore.GREEN + "Password entered successfully." + Style.RESET_ALL)

        # Submit login form
        password_field.send_keys(Keys.RETURN)
        input(Fore.LIGHTCYAN_EX + "After solving CAPTCHA (if any), press Enter to continue..." + Style.RESET_ALL)
        time.sleep(5)
        handle_captcha(driver)
        print(Fore.GREEN + "Login successful!" + Style.RESET_ALL)

        # Print cookies for reference
        cookies = driver.get_cookies()
        print(Fore.YELLOW + f"Cookies saved: {cookies}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error during login process: {e}" + Style.RESET_ALL)
        driver.quit()
        exit()

def click_on_comments():
    """Click on the comments button to open the comments section."""
    try:
        xpaths = [
            '//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/button[2]/span',
            '//*[@id="column-list-container"]/article[1]/div/section[2]/button[2]/span',
            '/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div[3]/button[2]/span'
        ]
        for xpath in xpaths:
            try:
                comment_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                comment_button.click()
                print(Fore.CYAN + "Comments section opened. Collecting commenter links..." + Style.RESET_ALL)
                handle_captcha(driver)
                break
            except TimeoutException:
                continue
        else:
            print(Fore.RED + "Comments button not found. Please click manually and press Enter..." + Style.RESET_ALL)
            input()
    except Exception as e:
        print(Fore.RED + f"Error while clicking on comments button: {e}" + Style.RESET_ALL)

def get_commenter_links(num_users):
    """Extract commenter profile links from the comments section."""
    commenter_links = []
    for i in range(1, num_users + 1):
        xpaths = [
            f"//*[@id='main-content-video_detail']/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[{i}]/div/div[2]/div[1]/div[1]/div/a",
            f'//*[@id="main-content-video_detail"]/div/div[2]/div[1]/div[2]/div[2]/div[{i}]/div/div[2]/div[1]/div[1]/div/a',
            f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/div[{i}]/div[1]/div[1]/a',
            f'/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div/div[{i}]/div[1]/div[1]/a',
            f'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[{i}]/div/div[2]/div[1]/div[1]/div/a'
        ]
        for xpath in xpaths:
            try:
                commenter_element = WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                link = commenter_element.get_attribute("href")
                if link:
                    commenter_links.append(link)
                    break
            except TimeoutException:
                continue
        else:
            print(Fore.RED + f"Could not extract link for commenter {i} using any provided XPaths." + Style.RESET_ALL)
    return commenter_links

def process_user(user_link, num_likes_per_user):
    """Process a commenter profile by liking a specified number of videos."""
    try:
        driver.get(user_link)
        print(Fore.CYAN + f"Opened profile: {user_link}" + Style.RESET_ALL)
        time.sleep(random.uniform(3, 5))
        handle_captcha(driver)
    except Exception as e:
        print(Fore.RED + f"Error opening profile {user_link}: {e}" + Style.RESET_ALL)
        return

    # Click on the first video in the profile
    try:
        first_video_xpath = '//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div/div/div/div'
        first_video = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, first_video_xpath))
        )
        first_video.click()
        print(Fore.CYAN + "Clicked on the first video." + Style.RESET_ALL)
        handle_captcha(driver)
    except TimeoutException:
        print(Fore.RED + "No videos found in this profile. Moving to the next user..." + Style.RESET_ALL)
        return

    # Like videos in the profile
    for i in range(num_likes_per_user):
        like_button_xpaths = [
            '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button[1]/span',
            '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/div/div[1]/div[1]/button[1]'
        ]
        like_button_found = False
        for xpath in like_button_xpaths:
            try:
                like_button = WebDriverWait(driver, 0.001).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                driver.execute_script("arguments[0].click();", like_button)
                print(Fore.GREEN + f"Liked video number {i+1} on this profile." + Style.RESET_ALL)
                like_button_found = True
                handle_captcha(driver)
                break
            except TimeoutException:
                continue
        
        if not like_button_found:
            print(Fore.RED + f"Like button not found for video {i+1}. Skipping..." + Style.RESET_ALL)
            continue

        # Move to the next video
        try:
            next_button_xpath = '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]'
            next_button = WebDriverWait(driver, 0.001).until(
                EC.element_to_be_clickable((By.XPATH, next_button_xpath))
            )
            driver.execute_script("arguments[0].click();", next_button)
            print(Fore.CYAN + "Moved to the next video." + Style.RESET_ALL)
            time.sleep(random.uniform(0.1, 0.5))
            handle_captcha(driver)
        except TimeoutException:
            print(Fore.RED + "Next button not found. Exiting loop for this user." + Style.RESET_ALL)
            break

# ------------------------ Main Program ------------------------

def main():
    print(Fore.MAGENTA + "=" * 60)
    print(Fore.MAGENTA + Style.BRIGHT + "          TikTok Commenter Liker".center(60))
    print(Fore.MAGENTA + "=" * 60 + Style.RESET_ALL)

    # Get user inputs
    username = input(Fore.LIGHTCYAN_EX + "Enter your TikTok username: " + Style.RESET_ALL)
    password = input(Fore.LIGHTCYAN_EX + "Enter your TikTok password: " + Style.RESET_ALL)
    video_url = input(Fore.LIGHTCYAN_EX + "Enter the TikTok video URL: " + Style.RESET_ALL)
    num_users = int(input(Fore.LIGHTCYAN_EX + "Enter number of commenters to process: " + Style.RESET_ALL))
    num_likes_per_user = int(input(Fore.LIGHTCYAN_EX + "Enter number of videos to like per user: " + Style.RESET_ALL))

    # Login to TikTok
    login(username, password)

    # Open the specified video URL
    driver.get(video_url)
    time.sleep(5)
    handle_captcha(driver)

    # Open the comments section
    click_on_comments()
    handle_captcha(driver)

    # Extract commenter links
    commenter_links = get_commenter_links(num_users)
    print(Fore.LIGHTYELLOW_EX + f"Total commenter links extracted: {len(commenter_links)}" + Style.RESET_ALL)

    # Process each commenter profile
    for idx, user_link in enumerate(commenter_links, start=1):
        print(Fore.BLUE + "-" * 60 + Style.RESET_ALL)
        print(Fore.BLUE + Style.BRIGHT + f"Processing user {idx}: {user_link}".center(60) + Style.RESET_ALL)
        print(Fore.BLUE + "-" * 60 + Style.RESET_ALL)
        process_user(user_link, num_likes_per_user)

    print(Fore.GREEN + "=" * 60 + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "All users processed. Exiting...".center(60) + Style.RESET_ALL)
    print(Fore.GREEN + "=" * 60 + Style.RESET_ALL)
    driver.quit()

if __name__ == "__main__":
    main()

