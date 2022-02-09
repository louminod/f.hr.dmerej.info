from playwright.sync_api import Playwright, sync_playwright


def test_employee_edit_address(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://f.hr.dmerej.info/
    page.goto("https://f.hr.dmerej.info/")
    # Click text=Add new employee
    page.click("text=Add new employee")
    # assert page.url == "https://f.hr.dmerej.info/add_employee"
    # Click input[name="name"]
    page.click("input[name=\"name\"]")
    # Fill input[name="name"]
    page.fill("input[name=\"name\"]", "tom")
    # Click input[name="email"]
    page.click("input[name=\"email\"]")
    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "tom@gmail.com")
    # Click input[name="address_line1"]
    page.click("input[name=\"address_line1\"]")
    # Fill input[name="address_line1"]
    page.fill("input[name=\"address_line1\"]", "5 rue de la paix")
    # Click input[name="address_line2"]
    page.click("input[name=\"address_line2\"]")
    # Fill input[name="address_line2"]
    page.fill("input[name=\"address_line2\"]", "appart 12")
    # Click input[name="city"]
    page.click("input[name=\"city\"]")
    # Fill input[name="city"]
    page.fill("input[name=\"city\"]", "Paris")
    # Click input[name="zip_code"]
    page.click("input[name=\"zip_code\"]")
    # Fill input[name="zip_code"]
    page.fill("input[name=\"zip_code\"]", "75000")
    # Click input[name="hiring_date"]
    page.click("input[name=\"hiring_date\"]")
    # Fill input[name="hiring_date"]
    page.fill("input[name=\"hiring_date\"]", "15/02/2021")
    # Click input[name="job_title"]
    page.click("input[name=\"job_title\"]")
    # Fill input[name="job_title"]
    page.fill("input[name=\"job_title\"]", "director")
    # Click button:has-text("Add")
    page.click("button:has-text(\"Add\")")
    # assert page.url == "https://f.hr.dmerej.info/employees"
    # Click text=tom tom@gmail.com no Edit Delete >> a
    page.click("text=tom tom@gmail.com no Edit Delete >> a")
    # assert page.url == "https://f.hr.dmerej.info/employee/267"
    # Click text=Update address
    page.click("text=Update address")
    # assert page.url == "https://f.hr.dmerej.info/employee/267/address"
    # Click input[name="address_line1"]
    page.click("input[name=\"address_line1\"]")
    # Click input[name="address_line1"]
    page.click("input[name=\"address_line1\"]")
    # Fill input[name="address_line1"]
    page.fill("input[name=\"address_line1\"]", "5 rue de la rue")
    # Click input[name="address_line2"]
    page.click("input[name=\"address_line2\"]")
    # Fill input[name="address_line2"]
    page.fill("input[name=\"address_line2\"]", "appart 15")
    # Click input[name="city"]
    page.click("input[name=\"city\"]")
    # Fill input[name="city"]
    page.fill("input[name=\"city\"]", "Par")
    # Click input[name="zip_code"]
    page.click("input[name=\"zip_code\"]")
    # Fill input[name="zip_code"]
    page.fill("input[name=\"zip_code\"]", "75012")
    # Click text=Update
    page.click("text=Update")
    # assert page.url == "https://f.hr.dmerej.info/employees"
    # Click text=tom tom@gmail.com no Edit Delete >> a
    page.click("text=tom tom@gmail.com no Edit Delete >> a")
    # assert page.url == "https://f.hr.dmerej.info/employee/267"
    # Click text=Update address
    page.click("text=Update address")
    # assert page.url == "https://f.hr.dmerej.info/employee/267/address"
    # ---------------------

    address = page.locator("input[name=\"address_line1\"]").input_value()
    address2 = page.locator("input[name=\"address_line2\"]").input_value()
    city = page.locator("input[name=\"city\"]").input_value()
    zip_code = page.locator("input[name=\"zip_code\"]").input_value()

    assert address == "5 rue de la rue"
    assert address2 == "appart 15"
    assert city == "Par"
    assert zip_code == "75012"

    context.close()
    browser.close()


def test_employee_edit_basic_info(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://f.hr.dmerej.info/
    page.goto("https://f.hr.dmerej.info/")
    # Click text=Add new employee
    page.click("text=Add new employee")
    # assert page.url == "https://f.hr.dmerej.info/add_employee"
    # Click input[name="name"]
    page.click("input[name=\"name\"]")
    # Fill input[name="name"]
    page.fill("input[name=\"name\"]", "tom")
    # Click input[name="email"]
    page.click("input[name=\"email\"]")
    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "tom@gmail.com")
    # Click input[name="address_line1"]
    page.click("input[name=\"address_line1\"]")
    # Fill input[name="address_line1"]
    page.fill("input[name=\"address_line1\"]", "5 rue de la paix")
    # Click input[name="address_line2"]
    page.click("input[name=\"address_line2\"]")
    # Fill input[name="address_line2"]
    page.fill("input[name=\"address_line2\"]", "appart 12")
    # Click input[name="city"]
    page.click("input[name=\"city\"]")
    # Fill input[name="city"]
    page.fill("input[name=\"city\"]", "Paris")
    # Click input[name="zip_code"]
    page.click("input[name=\"zip_code\"]")
    # Fill input[name="zip_code"]
    page.fill("input[name=\"zip_code\"]", "75000")
    # Click input[name="hiring_date"]
    page.click("input[name=\"hiring_date\"]")
    # Fill input[name="hiring_date"]
    page.fill("input[name=\"hiring_date\"]", "15/02/2021")
    # Click input[name="job_title"]
    page.click("input[name=\"job_title\"]")
    # Fill input[name="job_title"]
    page.fill("input[name=\"job_title\"]", "director")
    # Click button:has-text("Add")
    page.click("button:has-text(\"Add\")")
    # assert page.url == "https://f.hr.dmerej.info/employees"
    # Click text=tom tom@gmail.com no Edit Delete >> a
    page.click("text=tom tom@gmail.com no Edit Delete >> a")
    # assert page.url == "https://f.hr.dmerej.info/employee/277"
    # Click text=Update basic info
    page.click("text=Update basic info")
    # assert page.url == "https://f.hr.dmerej.info/employee/277/basic"
    # Click input[name="name"]
    page.click("input[name=\"name\"]")
    # Fill input[name="name"]
    page.fill("input[name=\"name\"]", "tomi")
    # Click input[name="email"]
    page.click("input[name=\"email\"]")
    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "tomi@gmail.com")
    # Click text=Update
    page.click("text=Update")
    # assert page.url == "https://f.hr.dmerej.info/employees"
    # Click text=tomi tomi@gmail.com no Edit Delete >> a
    page.click("text=tomi tomi@gmail.com no Edit Delete >> a")
    # assert page.url == "https://f.hr.dmerej.info/employee/277"
    # Click text=Update basic info
    page.click("text=Update basic info")
    # assert page.url == "https://f.hr.dmerej.info/employee/277/basic"
    # ---------------------

    name = page.locator("input[name=\"name\"]").input_value()
    email = page.locator("input[name=\"email\"]").input_value()

    assert name == "tomi"
    assert email == "tomi@gmail.com"

    context.close()
    browser.close()


def test_employee_edit_legal_info(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://f.hr.dmerej.info/
    page.goto("https://f.hr.dmerej.info/")
    # Click text=Add new employee
    page.click("text=Add new employee")
    # assert page.url == "https://f.hr.dmerej.info/add_employee"
    # Click input[name="name"]
    page.click("input[name=\"name\"]")
    # Fill input[name="name"]
    page.fill("input[name=\"name\"]", "tom")
    # Click input[name="email"]
    page.click("input[name=\"email\"]")
    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "tom@gmail.com")
    # Click input[name="address_line1"]
    page.click("input[name=\"address_line1\"]")
    # Fill input[name="address_line1"]
    page.fill("input[name=\"address_line1\"]", "5 rue de la paix")
    # Click input[name="address_line2"]
    page.click("input[name=\"address_line2\"]")
    # Fill input[name="address_line2"]
    page.fill("input[name=\"address_line2\"]", "appart 12")
    # Click input[name="city"]
    page.click("input[name=\"city\"]")
    # Fill input[name="city"]
    page.fill("input[name=\"city\"]", "Paris")
    # Click input[name="zip_code"]
    page.click("input[name=\"zip_code\"]")
    # Fill input[name="zip_code"]
    page.fill("input[name=\"zip_code\"]", "75000")
    # Click input[name="hiring_date"]
    page.click("input[name=\"hiring_date\"]")
    # Fill input[name="hiring_date"]
    page.fill("input[name=\"hiring_date\"]", "15/02/2021")
    # Click input[name="job_title"]
    page.click("input[name=\"job_title\"]")
    # Fill input[name="job_title"]
    page.fill("input[name=\"job_title\"]", "director")
    # Click button:has-text("Add")
    page.click("button:has-text(\"Add\")")
    # assert page.url == "https://f.hr.dmerej.info/employees"
    # Click text=tom tom@gmail.com no Edit Delete >> a
    page.click("text=tom tom@gmail.com no Edit Delete >> a")
    # assert page.url == "https://f.hr.dmerej.info/employee/281"
    # Click text=Update legal info
    page.click("text=Update legal info")
    # assert page.url == "https://f.hr.dmerej.info/employee/281/legal"
    # Click input[name="hiring_date"]
    page.click("input[name=\"hiring_date\"]")
    # Fill input[name="hiring_date"]
    page.fill("input[name=\"hiring_date\"]", "15/02/2022")
    # Click input[name="job_title"]
    page.click("input[name=\"job_title\"]")
    # Fill input[name="job_title"]
    page.fill("input[name=\"job_title\"]", "dir")
    # Click text=Update
    page.click("text=Update")
    # assert page.url == "https://f.hr.dmerej.info/employees"
    # Click tr:nth-child(154) td:nth-child(4) .btn
    page.click("tr:nth-child(154) td:nth-child(4) .btn")
    # assert page.url == "https://f.hr.dmerej.info/employee/281"
    # Click text=Update legal info
    page.click("text=Update legal info")
    # assert page.url == "https://f.hr.dmerej.info/employee/281/legal"
    # ---------------------

    hiring_date = page.locator("input[name=\"hiring_date\"]").input_value()
    job_title = page.locator("input[name=\"job_title\"]").input_value()

    assert hiring_date == "15/02/2022"
    assert job_title == "dir"

    context.close()
    browser.close()


def test_employee_delete(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://f.hr.dmerej.info/
    page.goto("https://f.hr.dmerej.info/")
    # Click text=Add new employee
    page.click("text=Add new employee")
    # assert page.url == "https://f.hr.dmerej.info/add_employee"
    # Click input[name="name"]
    page.click("input[name=\"name\"]")
    # Fill input[name="name"]
    page.fill("input[name=\"name\"]", "pomu")
    # Click input[name="email"]
    page.click("input[name=\"email\"]")
    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "pomu@gmail.com")
    # Click input[name="address_line1"]
    page.click("input[name=\"address_line1\"]")
    # Fill input[name="address_line1"]
    page.fill("input[name=\"address_line1\"]", "3 rue aeae")
    # Click input[name="address_line2"]
    page.click("input[name=\"address_line2\"]")
    # Fill input[name="address_line2"]
    page.fill("input[name=\"address_line2\"]", "zaezaeaze")
    # Click input[name="city"]
    page.click("input[name=\"city\"]")
    # Fill input[name="city"]
    page.fill("input[name=\"city\"]", "PAris")
    # Click input[name="zip_code"]
    page.click("input[name=\"zip_code\"]")
    # Fill input[name="zip_code"]
    page.fill("input[name=\"zip_code\"]", "75000")
    # Click input[name="hiring_date"]
    page.click("input[name=\"hiring_date\"]")
    # Fill input[name="hiring_date"]
    page.fill("input[name=\"hiring_date\"]", "12/12/12")
    # Click input[name="job_title"]
    page.click("input[name=\"job_title\"]")
    # Fill input[name="job_title"]
    page.fill("input[name=\"job_title\"]", "director")
    # Click button:has-text("Add")
    page.click("button:has-text(\"Add\")")
    # assert page.url == "https://f.hr.dmerej.info/employees"
    # Click text=pomu pomu@gmail.com no Edit Delete >> :nth-match(a, 2)
    page.click("text=pomu pomu@gmail.com no Edit Delete >> :nth-match(a, 2)")
    # assert page.url == "https://f.hr.dmerej.info/employee/delete/286"
    # Click text=Proceed
    page.click("text=Proceed")
    # assert page.url == "https://f.hr.dmerej.info/employees"
    # ---------------------

    visible = page.locator("text=pomu pomu@gmail.com no Edit Delete >> :nth-match(a, 2)").is_visible()

    assert visible == False

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_employee_edit_address(playwright)
    test_employee_edit_basic_info(playwright)
    test_employee_edit_legal_info(playwright)
    test_employee_delete(playwright)