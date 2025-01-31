# pylint: disable=C0103
import pytest
from common_utility.Utility import Utils as utility
from tests.limon_nextgen_tests.pages.login_page import LoginPage
from tests.limon_nextgen_tests.pages.home_page import HomePage
from tests.limon_nextgen_tests.pages.new_kit import NewKitPage


@pytest.mark.limon_regression
@pytest.mark.asyncio
async def test_create_order_from_kit_workflow(setup_page):
    """Test to verify the login functionality."""
    page = setup_page
    utils = utility(page)
    logger = await utils.setup_logging()

    logger.info("Starting the test_create_order_from_kit_workflow test")

    logger.info("Logging in")
    login_page = LoginPage(page)
    await login_page.login()

    logger.info("Creating a new kit")
    home_page = HomePage(page)
    await home_page.open_create_new_kit()
    new_kit_page = NewKitPage(page)
    await new_kit_page.create_new_kit()

    logger.info("Finished the test_create_order_from_kit_workflow test")
