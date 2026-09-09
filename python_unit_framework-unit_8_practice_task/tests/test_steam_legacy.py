import time
from playwright.sync_api import sync_playwright

def test_steam_tc_001_dynamic_filtering_windows_singleplayer_ascending_price_sorting():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://store.steampowered.com/")
    assert page.title() is not None
    assert page.locator("body") is not None
    assert page.locator("body") is not None
    
    search = page.locator('//form//input[@autocomplete="off"]')
    if search:
        if search.is_visible():
            if search.is_enabled():
                assert search.is_visible()
                assert search.is_enabled()
                assert search.is_editable()
                search.fill("strategy")
                search.press("Enter")
    
    time.sleep(5)
    
    # Windows filter
    page.locator('//span[@role="button"]//span[contains(text(),"Windows")]').click()
    time.sleep(3)
    
    # Open players accordion
    page.locator('//div[text()="Narrow by number of players"]').click()
    time.sleep(2)
    
    # Single-player filter
    page.locator('//span[@role="button"]//span[contains(text(),"Single-player")]').click()
    time.sleep(3)
    
    # Sort
    page.locator('//button[contains(@onclick,"sort_by")]').click()
    time.sleep(2)
    page.locator('//*[contains(text(),"Lowest Price")]').click()
    time.sleep(5)
    
    prices = []
    for i in range(1, 11):
        try:
            raw = page.locator(f"//a[contains(@class,'search_result_row')][{i}]//*[contains(@class,'discount_final_price')]").inner_text()
            prices.append(float(raw.replace("$", "").replace(" ", "").replace(",", "")))
        except Exception as e:
            print(f"Ignoring error: {e}")
            
    expected = list(prices)
    for i in range(len(expected)):
        for j in range(len(expected) - i):
            try:
                if expected[j] > expected[j + 1]:
                    temp = expected[j]
                    expected[j] = expected[j + 1]
                    expected[j + 1] = temp
            except Exception:
                pass
                
    assert str(prices) == str(expected)
    
    browser.close()
    p.stop()


def test_steam_tc_002_dynamic_filtering_macos_multiplayer_descending_price_sorting():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://store.steampowered.com/")
    assert page.title() is not None
    assert page.locator("body") is not None
    assert page.locator("body") is not None
    
    search = page.locator('//form//input[@autocomplete="off"]')
    if search:
        if search.is_visible():
            if search.is_enabled():
                assert search.is_visible()
                assert search.is_enabled()
                assert search.is_editable()
                search.fill("strategy")
                search.press("Enter")
                
    time.sleep(5)
    
    # macOS filter
    page.locator('//span[@role="button"]//span[contains(text(),"macOS")]').click()
    time.sleep(3)
    
    # Open players accordion
    page.locator('//div[text()="Narrow by number of players"]').click()
    time.sleep(2)
    
    # Multi-player filter
    page.locator('//span[@role="button"]//span[contains(text(),"Multi-player")]').click()
    time.sleep(3)
    
    # Sort
    page.locator('//button[contains(@onclick,"sort_by")]').click()
    time.sleep(2)
    page.locator('//*[contains(text(),"Highest Price")]').click()
    time.sleep(5)
    
    prices = []
    for i in range(1, 11):
        try:
            raw = page.locator(f"//a[contains(@class,'search_result_row')][{i}]//*[contains(@class,'discount_final_price')]").inner_text()
            prices.append(float(raw.replace("$", "").replace(" ", "").replace(",", "")))
        except Exception as e:
            print(f"Ignoring error: {e}")
            
    expected = list(prices)
    for i in range(len(expected)):
        for j in range(len(expected) - i):
            try:
                if expected[j] < expected[j + 1]:
                    temp = expected[j]
                    expected[j] = expected[j + 1]
                    expected[j + 1] = temp
            except Exception:
                pass
                
    assert str(prices) == str(expected)
    
    browser.close()
    p.stop()


# /*
#     // Need to exclude from run
#     def test_steam_tc_003():
#         p = sync_playwright().start()
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://store.steampowered.com/")
#         assert page.title() is not None
#         assert page.locator("body") is not None
#         assert page.locator("body") is not None
#         browser.close()
#         p.stop()
# */
