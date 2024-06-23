from pages.LOGIN.login_page import LoginPage
import pytest

from pages.utility2_page import BoardsWithActivityAndEngagementReports, Cards, EngCards, ImpactReportCards, \
    BoardWithImpactAndAttributeReports, \
    AttributeReportCards


class TestCreateReportCards:
    @pytest.fixture(autouse=True)
    def login(self, browser):
        # Instantiate the login page
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login()

    # --------------------------------Activity Engagement reports Board-----------------------------
    def test_create_board_activity_engagement_reports(self, browser):
        createBoard = BoardsWithActivityAndEngagementReports(browser)
        createBoard.create_board_activity_engagement_reports()

    # ----DELETE BOARD------
    def test_delete_board_activity_engagement_reports(self, browser):
        createBoard = BoardsWithActivityAndEngagementReports(browser)
        createBoard.search_and_delete_board_activity_engagement_reports()

    # --------------------------------Impact attribute reports Board---------------------------------

    def test_create_board_impact_attribute_reports(self, browser):
        createBoard2 = BoardWithImpactAndAttributeReports(browser)
        createBoard2.create_board_impact_attribute_reports()

    # ----DELETE BOARD------
    def test_delete_board_impact_attribute_reports(self, browser):
        createBoard = BoardWithImpactAndAttributeReports(browser)
        createBoard.search_and_delete_board_impact_attribute_reports()

    # --------------------Report Cards-----------------------------------------
    def test_add_all_activity_cards(self, browser):
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

    def test_add_item_curve_report_card(self, browser):
        reportCard = Cards(browser)
        reportCard.add_item_curve_report_card()

    def test_add_activity_over_time_report_card(self, browser):
        reportCard = Cards(browser)
        reportCard.add_activity_over_time_report_card()

    def test_add_activity_by_milestone_report_card(self, browser):
        reportCard = Cards(browser)
        reportCard.add_activity_by_milestone_report_card()

    def test_add_activity_by_person(self, browser):
        reportCard = Cards(browser)
        reportCard.add_activity_by_person()

    def test_add_activity_by_persona(self, browser):
        reportCard = Cards(browser)
        reportCard.add_activity_by_persona()

    def test_add_activity_by_location(self, browser):
        reportCard = Cards(browser)
        reportCard.add_activity_by_location()

    def test_add_activity_by_template(self, browser):
        reportCard = Cards(browser)
        reportCard.add_activity_by_template()

    def test_add_cycle_time_by_person(self, browser):
        reportCard = Cards(browser)
        reportCard.add_cycle_time_by_person()

    def test_add_cycle_time_by_location(self, browser):
        reportCard = Cards(browser)
        reportCard.add_cycle_time_by_location()

    def test_add_cycle_time_by_milestone(self, browser):
        reportCard = Cards(browser)
        reportCard.add_cycle_time_by_milestone()

    # createBoard.search_and_delete_board()
    def test_add_all_engagement_report_cards(self, browser):
        engCard = EngCards(browser)
        engCard.add_user_engagement_summary_report_card()
        engCard.add_user_participation_summary_report_card()
        engCard.add_engagement_by_location_report_card()
        engCard.add_engagement_by_persona()

    def test_user_engagement_summary(self, browser):
        engCard = EngCards(browser)
        engCard.add_user_engagement_summary_report_card()

    def test_user_participation_summary(self, browser):
        engCard = EngCards(browser)
        engCard.add_user_participation_summary_report_card()

    def test_engagement_by_location(self, browser):
        engCard = EngCards(browser)
        engCard.add_engagement_by_location_report_card()

    def test_engagement_by_persona(self, browser):
        engCard = EngCards(browser)
        engCard.add_engagement_by_persona()

    # -----------------Impact Reports---------------------

    # def test_create_board2(self, browser):
    #     createBoard2 = BoardWithImpactAndAttributeReports(browser)
    #     createBoard2.create_board_report2()

    # def test_delete_board2(self, browser):
    #     createBoard = BoardWithImpactAndAttributeReports(browser)
    #     createBoard.search_and_delete_board_reports2()

    def test_add_all_impact_report_cards(self, browser):
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

    def test_add_impact_summary_report_card(self, browser):
        impactCard = ImpactReportCards(browser)
        impactCard.add_impact_over_time_report_card()

    # -----------------Attribute Reports---------------------

    def test_add_all_attribute_report_cards(self, browser):
        attributeCard = AttributeReportCards(browser)
        attributeCard.add_attribute_summary_report_card()
        attributeCard.add_activity_by_attribute_report_card()
        attributeCard.add_impact_by_attribute_report_card()

    # ---------------ALL REPORTS ON TWO BOARDS--------------------------------------------

    def test_add_all_report_cards(self, browser):
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
