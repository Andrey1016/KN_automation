from selenium.webdriver.common.by import By


class HeaderLocators:
    HEADER_ADMIN = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Admin']")
    HEADER_CREATE_BTN = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Create']")
    HEADER_BOARDS = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Boards']")
    NOTIFICATIONS = (By.XPATH, "//span[contains(@class,'fas far fa-bell')]")


class CreateBtnItemsDropdown:
    ITEM_ADVANCED_AUTO_TEST = (By.XPATH, "//span[contains(@id, 'menuitem') and text()='5S Factory Audit']")
    ALL_ITEMS_CREATE = (
        By.XPATH, "//span[@class='x-menu-item-text x-menu-item-text-app-menu-white x-menu-item-indent-no-separator']")
    # ALL_ITEMS_CREATE_AND_FOLDERS = (By.XPATH, "//div[@class='x-menu-item x-menu-item-app-menu-white x-box-item']")


class CreateDeleteBoards:
    CREATE_BOARD = (By.XPATH, "//span[contains(@class,'x-btn-inne')and text()='Create Board']")
    BOARD_TITLE = (By.XPATH, "//input[@placeholder='Required']")
    BOARD_CREATE_BTN = (By.XPATH, "//span[contains(@class,'x-btn-inner x-btn-inner-de')and text()='Create']")
    BOARD_AUTOTEST = (
        By.XPATH, "//span[contains(@class,'x-menu-item-text')and text()='Board With Activity And Engagement Reports']")

    BOARD_ALL_CARDS = (
        By.XPATH, "//span[contains(@class,'x-menu-item-text')and text()='Board With ALL cards (except reports)']")
    BOARD_REPORT_CARDS2 = (
        By.XPATH, "//span[contains(@class,'x-menu-item-text')and text()='Board With Impact And Attribute Reports']")

    BOARD_ACTIONS_DROPDOWN = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Actions']")
    DELETE_BOARD = (By.XPATH, "//div[contains(@class,'x-menu')]//parent::span[text()='Delete Board']")
    #
    # manage_boards_btn = (By.XPATH, "//span[contains(@class,'x-btn-inner')and text()='Manage Boards']")
    #
    CHECKBOX_DELETE_BOARD = (By.XPATH, "//label[@data-ref='boxLabelEl' and contains(text(), 'I understand')]")
    DELETE_BOARD_BTN = (By.XPATH, "//span[@data-ref='btnInnerEl' and contains(text(), 'Delete')]")


class ReportCards:
    BOARDS_ADD_DROPDOWN = (By.XPATH, "//span[contains(@class,'x-btn-inner ')and text()='Add']")
    ADD_REPORT_CARD = (By.XPATH, "//span[contains(@class,'x-menu-item-text')and text()='Report']")
    ADD_ITEM_LIST_CARD = (By.XPATH, "//span[contains(@class,'x-menu-item-text')and text()='Item List']")
    REPORT_CARD_NAME = (By.CSS_SELECTOR, "[name='name']")
    REPORT_CARD_ADD = (By.XPATH,
                       "//div[@class='x-window-bodyWrap']//following-sibling::span[@class='x-btn-inner x-btn-inner-default-large']")

    ENGAGEMENT = (By.XPATH,
                  "//span[contains(@class, 'x-btn-inner') and contains(@class, 'x-btn-inner-default-medium') and text()='Engagement']")
    IMPACT = (By.XPATH,
              "//span[contains(@class, 'x-btn-inner') and contains(@class, 'x-btn-inner-default-medium') and text()='Impact']")
    ATTRIBUTE = (By.XPATH,
                 "//span[contains(@class, 'x-btn-inner') and contains(@class, 'x-btn-inner-default-medium') and text()='Attribute']")

    ITEM_CURVE = By.XPATH, "//span[text() = 'Item Curve']"
    ACTIVITY_OVER_TIME = (By.XPATH, "//span[text() = 'Activity Over Time']")
    ACTIVITY_BY_MILESTONE = (By.XPATH, "//span[text() = 'Activity by Milestone']")
    ACTIVITY_BY_PERSON = (By.XPATH, "//span[text() = 'Activity by Person']")
    ACTIVITY_BY_PERSONA = (By.XPATH, "//span[text() = 'Activity by Persona']")
    ACTIVITY_BY_LOCATION = (By.XPATH, "//span[text() = 'Activity by Location']")
    ACTIVITY_BY_TEMPLATE = (By.XPATH, "//span[text() = 'Activity by Template']")
    CYCLE_TIME_BY_PERSON = (By.XPATH, "//span[text() = 'Cycle Time by Person']")
    CYCLE_TIME_BY_LOCATION = (By.XPATH, "//span[text() = 'Cycle Time by Location']")
    CYCLE_TIME_BY_MILESTONE = (By.XPATH, "//span[text() = 'Cycle Time by Milestone']")

    USER_ENGAGEMENT_SUMMARY = (By.XPATH,
                               "//span[text() = 'User Engagement Summary' and @class='x-btn-inner x-btn-inner-app-header-button-l-large']")
    USER_PARTICIPATION_SUMMARY = (By.XPATH, "//span[text() = 'User Participation Summary']")
    ENGAGEMENT_BY_LOCATION = (By.XPATH, "//span[text() = 'Engagement by Location']")
    ENGAGEMENT_BY_PERSONA = (By.XPATH, "//span[text() = 'Engagement by Persona']")

    IMPACT_SUMMARY = (By.XPATH, "//span[text() = 'Impact Summary']")
    IMPACT_OVER_TIME = (By.XPATH, "//span[text() = 'Impact Over Time']")
    IMPACT_BY_PERSON = (By.XPATH, "//span[text() = 'Impact by Person']")
    IMPACT_BY_LOCATION = (By.XPATH, "//span[text() = 'Impact by Location']")
    IMPACT_BY_ITEM = (By.XPATH, "//span[text() = 'Impact by Item']")
    IMPACT_BY_IMPACT_VALUE = (By.XPATH, "//span[text() = 'Impact by Impact Value']")
    IMPACT_BY_MILESTONE = (By.XPATH, "//span[text() = 'Impact by Milestone']")

    ATTRIBUTE_SUMMARY = (By.XPATH, "//span[text() = 'Attribute Summary']")
    ACTIVITY_BY_ATTRIBUTE = (By.XPATH, "//span[text() = 'Activity by Attribute']")
    IMPACT_BY_ATTRIBUTE = (By.XPATH, "//span[text() = 'Impact by Attribute']")


class ItemListCard:
    ADD_ITEM_LIST_CARD = (By.XPATH, "//span[contains(@class,'x-menu-item-text')and text()='Item List']")
    FILTER_CRITERIA = (By.CSS_SELECTOR, ".x-form-trigger.x-form-trigger-default.x-form-trigger-click")
