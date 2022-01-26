
def test_insert_employee(page) -> None:

        # Go to https://f.hr.dmerej.info/
        page.goto("https://f.hr.dmerej.info/")
        # Click text=Add new employee
        page.click("text=Add new employee")
        # assert page.url == "https://f.hr.dmerej.info/add_employee"
        # Click input[name="name"]
        page.click("input[name=\"name\"]")
        # Fill input[name="name"]
        page.fill("input[name=\"name\"]", "Bobby")
        # Press Tab
        page.press("input[name=\"name\"]", "Tab")
        # Fill input[name="email"]
        page.fill("input[name=\"email\"]", "Bob@bob.com")
        # Click input[name="address_line1"]
        page.click("input[name=\"address_line1\"]")
        # Fill input[name="address_line1"]
        page.fill("input[name=\"address_line1\"]", "1 Rue bob")
        # Click input[name="address_line2"]
        page.click("input[name=\"address_line2\"]")
        # Fill input[name="address_line2"]
        page.fill("input[name=\"address_line2\"]", "bob")
        # Click input[name="city"]
        page.click("input[name=\"city\"]")
        # Fill input[name="city"]
        page.fill("input[name=\"city\"]", "Bob city")
        # Click input[name="zip_code"]
        page.click("input[name=\"zip_code\"]")
        # Fill input[name="zip_code"]
        page.fill("input[name=\"zip_code\"]", "45200")
        # Click input[name="hiring_date"]
        page.click("input[name=\"hiring_date\"]")
        # Fill input[name="hiring_date"]
        page.fill("input[name=\"hiring_date\"]", "11/11/11")
        # Click input[name="job_title"]
        page.click("input[name=\"job_title\"]")
        # Fill input[name="job_title"]
        page.fill("input[name=\"job_title\"]", "Testeur")
        # Click button:has-text("Add")
        page.click("button:has-text(\"Add\")")
        # assert page.url == "https://f.hr.dmerej.info/employees"

        name = page.locator("tr >> nth=-1 >> td >> nth=0").inner_html()
        email = page.locator("tr >> nth=-1 >> td >> nth=1").inner_html()

        assert name == "Bobby"
        assert email == "Bob@bob.com"
