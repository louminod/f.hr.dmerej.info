

def add_employee(page, name, mail, adr1, adr2, city, zip, date, job):
        # Go to https://f.hr.dmerej.info/
        page.goto("https://f.hr.dmerej.info/")
        # Click text=Add new employee
        page.click("text=Add new employee")
        # assert page.url == "https://f.hr.dmerej.info/add_employee"
        # Click input[name="name"]
        page.click("input[name=\"name\"]")
        # Fill input[name="name"]
        page.fill("input[name=\"name\"]", name)
        # Press Tab
        page.press("input[name=\"name\"]", "Tab")
        # Fill input[name="email"]
        page.fill("input[name=\"email\"]", mail)
        # Click input[name="address_line1"]
        page.click("input[name=\"address_line1\"]")
        # Fill input[name="address_line1"]
        page.fill("input[name=\"address_line1\"]", adr1)
        # Click input[name="address_line2"]
        page.click("input[name=\"address_line2\"]")
        # Fill input[name="address_line2"]
        page.fill("input[name=\"address_line2\"]", adr2)
        # Click input[name="city"]
        page.click("input[name=\"city\"]")
        # Fill input[name="city"]
        page.fill("input[name=\"city\"]", city)
        # Click input[name="zip_code"]
        page.click("input[name=\"zip_code\"]")
        # Fill input[name="zip_code"]
        page.fill("input[name=\"zip_code\"]", zip)
        # Click input[name="hiring_date"]
        page.click("input[name=\"hiring_date\"]")
        # Fill input[name="hiring_date"]
        page.fill("input[name=\"hiring_date\"]", date)
        # Click input[name="job_title"]
        page.click("input[name=\"job_title\"]")
        # Fill input[name="job_title"]
        page.fill("input[name=\"job_title\"]", job)
        # Click button:has-text("Add")
        page.click("button:has-text(\"Add\")")
        # assert page.url == "https://f.hr.dmerej.info/employees"

#retrieve name, mail, job and hiring date of the last added employee
def employee_last_info(page):
        page.goto("https://f.hr.dmerej.info/employees")
        name = page.locator("tr >> nth=-1 >> td >> nth=0").inner_html()
        email = page.locator("tr >> nth=-1 >> td >> nth=1").inner_html()

        page.click("tr >> nth=-1 >> td >> nth=3 >> .btn")

        job = page.locator("p >> nth=1").inner_html()[:-1]
        date = page.locator("p >> nth=2").inner_html()[9:]
        
        page.click("text=Update address")


        return name, email, job, date



def test_insert_employee(page) -> None:

        add_employee(page, "Bobby", "Bob@bob.com", "1 rue bonjour", "none", "Bob city", "45210", "11/11/11", "tester")

        # name = page.locator("tr >> nth=-1 >> td >> nth=0").inner_html()
        # email = page.locator("tr >> nth=-1 >> td >> nth=1").inner_html()

        name , email, job, date = employee_last_info(page)

        assert name == "Bobby"
        assert email == "Bob@bob.com"
        assert job == "tester"
        assert date == "11/11/11"
