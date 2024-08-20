import pytest

from pages.LOGIN.login_page import LoginPage
from pages.utility2_page import CreateAllItems
from pages.HEADER.notifications.notifications_page import ClearNotifications
from pages.utility2_page import BoardsWithActivityAndEngagementReports, Cards, EngCards, ImpactReportCards, \
    BoardWithImpactAndAttributeReports, \
    AttributeReportCards
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def login(browser):
    # Instantiate the login page
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login()


def test_clear_notifications(browser):
    notifications = ClearNotifications(browser)
    notifications.clear_notifications()


def test_create_items(browser):
    create_item = CreateAllItems(browser)
    create_item.create_item()


def test_add_all_report_cards(browser):
    createBoard = BoardsWithActivityAndEngagementReports(browser)
    createBoard.create_board_activity_engagement_reports()

    reportCard = Cards(browser)
    reportCard.add_item_curve_report_card()
    reportCard.add_activity_over_time_report_card()
    reportCard.add_activity_by_milestone_report_card()
    reportCard.add_activity_by_person()
    reportCard.add_activity_by_persona()
    reportCard.add_activity_by_location()
    reportCard.add_activity_by_template()
    reportCard.add_cycle_time_by_person()
    reportCard.add_cycle_time_by_location()
    reportCard.add_cycle_time_by_milestone()

    engCard = EngCards(browser)
    engCard.add_user_engagement_summary_report_card()
    engCard.add_user_participation_summary_report_card()
    engCard.add_engagement_by_location_report_card()
    engCard.add_engagement_by_persona()

    createBoard2 = BoardWithImpactAndAttributeReports(browser)
    createBoard2.create_board_impact_attribute_reports()
    impactCard = ImpactReportCards(browser)
    impactCard.add_impact_summary_report_card()
    impactCard.add_impact_over_time_report_card()
    impactCard.add_impact_by_person_report_card()
    impactCard.add_impact_by_location()
    impactCard.add_impact_by_item_report_card()
    impactCard.add_impact_by_impact_value_report_card()
    impactCard.add_impact_by_milestone_report_card()

    attributeCard = AttributeReportCards(browser)
    attributeCard.add_attribute_summary_report_card()
    attributeCard.add_activity_by_attribute_report_card()
    attributeCard.add_impact_by_attribute_report_card()


def test_delete_board_activity_engagement_reports(browser):
    createBoard = BoardsWithActivityAndEngagementReports(browser)
    createBoard.search_and_delete_board_activity_engagement_reports()


def test_delete_board_impact_attribute_reports(browser):
    createBoard = BoardWithImpactAndAttributeReports(browser)
    createBoard.search_and_delete_board_impact_attribute_reports()
