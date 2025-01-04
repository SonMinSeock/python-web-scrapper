websites = (
    "goggle.com",
    "https://airbnb.com",
    "twitter.com",
    "facebook.com",
    "https://tiktok.com"
) 

for website in websites:
    if not website.startswith("https://") or not website.startswith("http://"):
        website = f"https://{website}"
    print(website)