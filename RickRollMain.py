import webbrowser, time, random
url = "https://youtu.be/dQw4w9WgXcQ"
for i in range(100):
    webbrowser.open_new_tab(url)
    time.sleep(random.randint(10, 300))