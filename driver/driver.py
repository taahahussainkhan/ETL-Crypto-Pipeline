import undetected_chromedriver as uc
from selenium_stealth import stealth




def gen_driver():
    try:
        print("Initializing driver...")

        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.36"
        chrome_options = uc.ChromeOptions()

        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("user-agent={}".format(user_agent))

        driver = uc.Chrome(options=chrome_options)

        print("Driver initialized successfully!")

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True
        )

        print("Stealth mode applied successfully!")

        return driver
    except Exception as e:
        print("Error in Driver: ",e)