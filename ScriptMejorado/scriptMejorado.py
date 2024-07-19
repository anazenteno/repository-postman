from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    """Setup the WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def add_task(driver, task_name):
    """Add a new task to the todo list."""
    task_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "new-task"))
    )
    task_input.send_keys(task_name)

    #TODO Validar la importancia de este Keys.return
    task_input.send_keys(Keys.RETURN)


def get_all_task(driver):
    """Retrieve all tasks name in the todo list."""
    return WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "task"))
    )


def main():
    driver = setup_driver()
    try:
        driver.get("http://todolistapp.com")

        task_name = "Buy groceries"
        # Adding a new task
        add_task(driver, task_name)

        # Checking if the task was added
        tasks = get_all_task(driver)
        task_len_old = len(tasks)
        assert any(task.text == task_name for task in tasks), "Task 'Buy groceries' not found in the list"

        # Add another task and check
        # task1_name = "Read a book"
        add_task(driver, task_name)
        tasks = get_all_task(driver)
        assert any(task.text == task_name for task in tasks), "Task 'Buy groceries' not found in the list"

        # Validate task list increment 1 task
        assert task_len_old + 1 == len(tasks), "List task not increment 1 task in the list"

    finally:
        driver.quit()


if _name_ == "_main_":
    main()