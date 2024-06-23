from pages.LOGIN.login_page import LoginPage
import pytest

from pages.utility2_page import BoardsWithActivityAndEngagementReports, Cards, EngCards, ImpactReportCards, \
    BoardWithImpactAndAttributeReports, \
    AttributeReportCards, BoardsAllCards


class TestCreateReportCards:
    @pytest.fixture(autouse=True)
    def login(self, browser):
        # Instantiate the login page
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login()

    # --------------------------------Activity Engagement reports Board-----------------------------
    def test_create_item_list_card(self, browser):
        createBoard = BoardsAllCards(browser)
        createBoard.create_board_with_all_cards()


