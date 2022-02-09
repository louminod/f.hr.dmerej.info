from playwright.sync_api import Playwright, sync_playwright

def test_delete_team(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://f.hr.dmerej.info/
    page.goto("https://f.hr.dmerej.info/")
    # Click text=Create new team
    page.click("text=Create new team")
    # assert page.url == "https://f.hr.dmerej.info/add_team"
    # Click input[name="name"]
    page.click("input[name=\"name\"]")
    # Fill input[name="name"]
    page.fill("input[name=\"name\"]", "TTT")
    # Click text=Add
    page.click("text=Add")
    # assert page.url == "https://f.hr.dmerej.info/teams"
    # Click text=TTT
    page.click("text=TTT")
    # Click :nth-match(:text("Delete"), 2)
    page.click(":nth-match(:text(\"Delete\"), 2)")
    # assert page.url == "https://f.hr.dmerej.info/team/delete/23"
    # Click text=Proceed
    page.click("text=Proceed")
    # assert page.url == "https://f.hr.dmerej.info/teams"
    # ---------------------

    visible = page.locator("text=TTT View members Delete").is_visible()

    assert visible == False

    context.close()
    browser.close()

with sync_playwright() as playwright:
    test_delete_team(playwright)