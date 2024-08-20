from selenium.webdriver.common.by import By


class ItemCreateWindow:
    ITEM_TITLE = (
        By.XPATH, "//input[@name='summary']")

    TEXT_AREA = (
        By.XPATH, "//div[@class='fr-element fr-view fr-element-scroll-visible']")

    TEXT_FIELDS = (
        By.XPATH,
        "//input[contains(@aria-describedby, 'textfield-') and contains(@class, 'x-form-empty-field')]")

    NUMBER_FIELDS = (
        By.XPATH,
        "//input[contains(@aria-describedby, 'numberfield-') and contains(@class, 'x-form-') and contains(@name, 'numberfield-')]")

    ALL_ATTRIBUTES = (
        By.XPATH,
        "//div[@class='x-field app-tag-field x-form-item x-form-item-default x-form-type-text x-box-item x-field-default x-vbox-form-item app-textfield']")

    FIRST_VALUE_ATTRIBUTE = (
        By.XPATH, "//div[contains(@class, 'x-boundlist-item') and position()=1]")

    ATTRIBUTE_NOTE = (
        By.XPATH, "//div[@style='min-height: 250px;']")

    SAVE_ATTRIBUTE_BTN = (
        By.XPATH, "//span[@class='x-btn-inner x-btn-inner-default-large']")

    DATE_FIELD = (
        By.XPATH,
        "//input[contains(@aria-describedby, 'datefield-') and contains(@name, 'datefield-') and contains(@aria-hidden, 'false')]")
    DUE_DATE_FIELD = (
        By.XPATH,
        "//input[contains(@aria-describedby, 'datefield-') and contains(@name, 'datefield-') and contains (@placeholder, 'Required')]")
    REVIEW_BY_DATE_FIELD = (
        By.XPATH, "//input[contains(@name, 'reviewDate')]")

    # =============TEAM======================

    RESPONSIBLE = (By.XPATH, "//label[text()='Required']")
    # -------------------------
    SPONSOR = (By.XPATH, "//div[label//span[text()='Sponsor(s):']]//label[text()='None']")
    # -------------------------
    API_AUTOTEST_USER_SPONSOR = (By.XPATH, "//div[contains(@data-qtip, 'rrippey7@gmail.com')]")

    API_AUTOTEST_USER_RESPONSIBLE = (By.XPATH, "//div[contains(@data-qtip, 'AutotestUser@gmaik.con')]")

    # =============STATUSES==================

    ACTIVE_STATUS_BTN = (By.XPATH, "//span[@class='x-btn-inner x-btn-inner-default-toolbar-small' and text()='Active']")

    DEFERRED_STATUS_BTN = (By.XPATH, "//span[@class='x-btn-inner x-btn-inner-default-toolbar-small' and text()='Deferred']")

    CREATE_ITEM_BTN = (By.XPATH, "//span[@class='x-btn-inner x-btn-inner-default-large' and text()='Create']")

    VIEW_ITEM_CLICK = (By.XPATH, "//span[@class='x-btn-inner x-btn-inner-default-large' and text()='View Item']")

    SUCCESS_WINDOW_CLOSE = (
        By.XPATH,
        "//a[@class='x-btn app-item-window-close-button x-unselectable x-box-item x-toolbar-item x-btn-app-header-button-s-small']")

    SUCCESS_WINDOW_ITEM_LINK = (
        By.XPATH, "//a[@class='open-modal app-toast-link']")

    CLOSE_ITEM = (By.XPATH, "//a[@class='x-btn app-item-window-close-button x-unselectable x-box-item x-btn-app-header-button-s-small x-btn-after-title']")

