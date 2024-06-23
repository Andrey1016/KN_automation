# import time
# from _pydatetime import timedelta
# from datetime import datetime, timezone
# from locators.HEADER_LOCATORS.header_page_locators import HeaderLocators, CreateBtnItemsDropdown, CreateDeleteBoards, \
#     CreateDeleteBoards, ReportCards
# from locators.ITEM_CREATE_WINDOW_LOCATORS.item_create_window_locators import ItemCreateWindow
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from pages.base_page import BasePage
# import logging
#
#
# # ================================ Item Create - Boards create - All report cards Create =================================
# def future_timestamp(days=6):
#     current_utc_time = datetime.now(timezone.utc)
#     future_utc_time = current_utc_time + timedelta(days=days)
#     future_utc_time.utctime("%Y, %b %d %-I:%M %p")
#     return future_utc_time
#
#
# def current_timestamp():
#     current_time = datetime.now()
#     formatted_time = current_time.strftime("%Y, %b %d %-I:%M %p")
#     return formatted_time
#
#
# class CreateAllItems(BasePage):
#     header_locators = HeaderLocators()
#     create_btn_locators = CreateBtnItemsDropdown()
#     locators = ItemCreateWindow()
#
#     def create_item(self):
#         self.element_is_visible(self.header_locators.HEADER_CREATE_BTN).click()
#
#         items = self.elements_are_present(self.create_btn_locators.ALL_ITEMS_CREATE)
#         items.sort(key=lambda e: e.location['y'])
#
#         for item in items:
#             item.click()
#
#             self.element_is_visible(self.locators.ITEM_TITLE).send_keys("AutoTest")
#
#             self.fill_text_areas()
#
#             self.fill_text_fields()
#
#             self.fill_number_fields()
#
#             self.add_all_attributes()
#
#             self.fill_date_filed()
#
#             self.element_is_visible(self.locators.CREATE_ITEM_BTN).click()
#
#             self.try_close_success_window()
#
#             self.element_is_visible(self.header_locators.HEADER_CREATE_BTN).click()
#
#     def fill_text_areas(self):
#         try:
#             text_areas = self.elements_are_present2(self.locators.TEXT_AREA)
#             for text_area in text_areas:
#                 text_area.send_keys(
#                     "Praesent vitae quam ultrices, ultrices purus quis, pulvinar erat. Sed elit sem, molestie id turpis in, elementum hendrerit nulla. Nullam fermentum massa vel urna congue, et facilisis urna bibendum. Vestibulum posuere risus ex, sed fermentum erat vehicula non. Curabitur ut neque quis orci hendrerit blandit. Morbi in.")
#         except NoSuchElementException:
#             pass
#
#     def fill_text_fields(self):
#         try:
#             text_fields = self.elements_are_present2(self.locators.TEXT_FIELDS)
#             for text_field in text_fields:
#                 text_field.send_keys("Text Field")
#         except NoSuchElementException:
#             pass
#
#     def fill_number_fields(self):
#         try:
#             number_fields = self.elements_are_present2(self.locators.NUMBER_FIELDS)
#             for number_field in number_fields:
#                 number_field.send_keys(987654321)
#         except NoSuchElementException:
#             pass
#
#     def try_close_success_window(self):
#         try:
#             self.element_is_visible(self.locators.SUCCESS_WINDOW_CLOSE).click()
#         except NoSuchElementException:
#             pass
#
#     def add_all_attributes(self):
#         try:
#             while True:
#                 dropdowns = self.elements_are_present2(self.locators.ALL_ATTRIBUTES)
#                 if not dropdowns:
#                     break
#
#                 dropdown = dropdowns.pop(0)
#                 dropdown.click()
#                 time.sleep(1.5)
#
#                 first_option = self.element_is_clickable(self.locators.FIRST_VALUE_ATTRIBUTE)
#                 if first_option:
#                     first_option.click()
#                     time.sleep(1.5)
#
#                     if self.element_is_present(self.locators.ATTRIBUTE_NOTE):
#                         note_field = self.element_is_visible(self.locators.ATTRIBUTE_NOTE)
#                         note_field.send_keys("test note")
#                         time.sleep(1.5)
#
#         except NoSuchElementException:
#             pass
#         except Exception as e:
#             print(f" {e} Created")
#
#     def fill_date_filed(self):
#         try:
#             date_fields = self.elements_are_present2(self.locators.DATE_FIELD)
#             for date_fields in date_fields:
#                 date_fields.send_keys(current_timestamp())
#         except NoSuchElementException:
#             pass
#
# #     =======================================All Items in ACTIVE status=======================================
#
#     def create_item_active_status(self):
#         self.element_is_visible(self.header_locators.HEADER_CREATE_BTN).click()
#
#         items = self.elements_are_present(self.create_btn_locators.ALL_ITEMS_CREATE)
#         items.sort(key=lambda e: e.location['y'])
#
#         for item in items:
#             item.click()
#
#             self.element_is_visible(self.locators.ITEM_TITLE).send_keys("AutoTest")
#
#             self.fill_text_areas()
#
#             self.fill_text_fields()
#
#             self.fill_number_fields()
#
#             self.add_all_attributes()
#
#             self.fill_date_filed()
#
#             self.element_is_clickable(self.locators.ACTIVE_STATUS_BTN).click()
#
#             self.element_is_visible(self.locators.CREATE_ITEM_BTN).click()
#
#             self.try_close_success_window()
#
#             self.element_is_visible(self.header_locators.HEADER_CREATE_BTN).click()
#
#     def fill_text_areas(self):
#         try:
#             text_areas = self.elements_are_present2(self.locators.TEXT_AREA)
#             for text_area in text_areas:
#                 text_area.send_keys(
#                     "Praesent vitae quam ultrices, ultrices purus quis, pulvinar erat. Sed elit sem, molestie id turpis in, elementum hendrerit nulla. Nullam fermentum massa vel urna congue, et facilisis urna bibendum. Vestibulum posuere risus ex, sed fermentum erat vehicula non. Curabitur ut neque quis orci hendrerit blandit. Morbi in.")
#         except NoSuchElementException:
#             pass
#
#     def fill_text_fields(self):
#         try:
#             text_fields = self.elements_are_present2(self.locators.TEXT_FIELDS)
#             for text_field in text_fields:
#                 text_field.send_keys("Text Field")
#         except NoSuchElementException:
#             pass
#
#     def fill_number_fields(self):
#         try:
#             number_fields = self.elements_are_present2(self.locators.NUMBER_FIELDS)
#             for number_field in number_fields:
#                 number_field.send_keys(987654321)
#         except NoSuchElementException:
#             pass
#
#     def try_close_success_window(self):
#         try:
#             self.element_is_visible(self.locators.SUCCESS_WINDOW_CLOSE).click()
#         except NoSuchElementException:
#             pass
#
#     def add_all_attributes(self):
#         try:
#             while True:
#                 dropdowns = self.elements_are_present2(self.locators.ALL_ATTRIBUTES)
#                 if not dropdowns:
#                     break
#
#                 dropdown = dropdowns.pop(0)
#                 dropdown.click()
#                 time.sleep(1.5)
#
#                 first_option = self.element_is_clickable(self.locators.FIRST_VALUE_ATTRIBUTE)
#                 if first_option:
#                     first_option.click()
#                     time.sleep(1.5)
#
#                     if self.element_is_present(self.locators.ATTRIBUTE_NOTE):
#                         note_field = self.element_is_visible(self.locators.ATTRIBUTE_NOTE)
#                         note_field.send_keys("test note")
#                         time.sleep(1.5)
#
#         except NoSuchElementException:
#             pass
#         except Exception as e:
#             print(f" {e} Created")
#
#     def fill_date_filed(self):
#         try:
#             date_fields = self.elements_are_present2(self.locators.DATE_FIELD)
#             for date_fields in date_fields:
#                 date_fields.send_keys(current_timestamp())
#         except NoSuchElementException:
#             pass
#
# # =======================================Boards for reports create and Delete=================================================
#
# class BoardsWithActivityAndEngagementReports(BasePage):
#     header_locators = HeaderLocators()
#     create_delete_board_locators = CreateDeleteBoards()
#
#     def create_board_activity_engagement_reports(self):
#         self.element_is_visible(self.header_locators.HEADER_BOARDS).click()
#         self.element_is_visible(self.create_delete_board_locators.CREATE_BOARD).click()
#         self.element_is_visible(self.create_delete_board_locators.BOARD_TITLE).send_keys(
#             "Board With Activity And Engagement Reports")
#         self.element_is_visible(self.create_delete_board_locators.BOARD_CREATE_BTN).click()
#         time.sleep(1)
#
#     def search_and_delete_board_activity_engagement_reports(self):
#
#         while True:
#             try:
#                 self.element_is_visible(self.header_locators.HEADER_BOARDS).click()
#                 self.element_is_visible(self.create_delete_board_locators.BOARD_AUTOTEST).click()
#             except (NoSuchElementException, TimeoutException):
#                 print("Boards have been deleted")
#                 break
#             self.element_is_visible(self.create_delete_board_locators.BOARD_ACTIONS_DROPDOWN).click()
#             self.element_is_visible(self.create_delete_board_locators.DELETE_BOARD).click()
#             self.element_is_visible(self.create_delete_board_locators.CHECKBOX_DELETE_BOARD).click()
#             self.element_is_visible(self.create_delete_board_locators.DELETE_BOARD_BTN).click()
#             time.sleep(1.5)
#
#
# class BoardWithImpactAndAttributeReports(BasePage):
#     header_locators = HeaderLocators()
#     create_delete_board_locators = CreateDeleteBoards()
#
#     def create_board_impact_attribute_reports(self):
#         self.element_is_visible(self.header_locators.HEADER_BOARDS).click()
#         self.element_is_visible(self.create_delete_board_locators.CREATE_BOARD).click()
#         self.element_is_visible(self.create_delete_board_locators.BOARD_TITLE).send_keys(
#             "Board With Impact And Attribute Reports")
#         self.element_is_visible(self.create_delete_board_locators.BOARD_CREATE_BTN).click()
#         time.sleep(1)
#
#     def search_and_delete_board_impact_attribute_reports(self):
#         while True:
#             try:
#                 self.element_is_visible(self.header_locators.HEADER_BOARDS).click()
#                 self.element_is_visible(self.create_delete_board_locators.BOARD_REPORT_CARDS2).click()
#             except (NoSuchElementException, TimeoutException):
#                 print("Boards have been deleted")
#                 break
#             self.element_is_visible(self.create_delete_board_locators.BOARD_ACTIONS_DROPDOWN).click()
#             self.element_is_visible(self.create_delete_board_locators.DELETE_BOARD).click()
#             self.element_is_visible(self.create_delete_board_locators.CHECKBOX_DELETE_BOARD).click()
#             self.element_is_visible(self.create_delete_board_locators.DELETE_BOARD_BTN).click()
#             time.sleep(1.5)
#
#
# class Cards(BasePage):
#     header_locators = HeaderLocators()
#     create_delete_board_locators = CreateDeleteBoards()
#     cards_locators = ReportCards()
#
#     def navigate_to_board(self):
#         try:
#             self.element_is_visible(self.header_locators.HEADER_BOARDS).click()
#             self.element_is_visible(self.create_delete_board_locators.BOARD_AUTOTEST).click()
#         except NoSuchElementException:
#             logging.error("AUTOTEST board is not accessible.")
#             raise
#
#     def add_report_card(self, report_type_locator, report_name):
#         self.element_is_visible(self.cards_locators.BOARDS_ADD_DROPDOWN).click()
#         self.element_is_visible(self.cards_locators.ADD_REPORT_CARD).click()
#         self.element_is_visible(report_type_locator).click()  # Select the specific report type
#         self.element_is_visible(self.cards_locators.REPORT_CARD_NAME).send_keys(report_name)
#         self.element_is_visible(self.cards_locators.REPORT_CARD_ADD).click()  # Click on the 'Add Report Card' button
#
#     def add_card_to_board(self, report_type_locator, report_name):
#
#         self.navigate_to_board()
#         self.add_report_card(report_type_locator, report_name)
#
#     def add_item_curve_report_card(self):
#         self.add_card_to_board(self.cards_locators.ITEM_CURVE, "Item Curve Report card")
#
#     def add_activity_over_time_report_card(self):
#         self.add_card_to_board(self.cards_locators.ACTIVITY_OVER_TIME, "Activity Over time Report card")
#
#     def add_activity_by_milestone_report_card(self):
#         self.add_card_to_board(self.cards_locators.ACTIVITY_BY_MILESTONE, "Activity by Milestone Report card")
#
#     def add_activity_by_person(self):
#         self.add_card_to_board(self.cards_locators.ACTIVITY_BY_PERSON, "Activity by Person Report card")
#
#     def add_activity_by_persona(self):
#         self.add_card_to_board(self.cards_locators.ACTIVITY_BY_PERSONA, "Activity by Persona Report card")
#
#     def add_activity_by_location(self):
#         self.add_card_to_board(self.cards_locators.ACTIVITY_BY_LOCATION, "Activity by Location Report card")
#
#     def add_activity_by_template(self):
#         self.add_card_to_board(self.cards_locators.ACTIVITY_BY_TEMPLATE, "Activity by Template Report card")
#
#     def add_cycle_time_by_person(self):
#         self.add_card_to_board(self.cards_locators.CYCLE_TIME_BY_PERSON, " Cycle time by person Report card")
#
#     def add_cycle_time_by_location(self):
#         self.add_card_to_board(self.cards_locators.CYCLE_TIME_BY_LOCATION, "Cycle time by Location Report card")
#
#     def add_cycle_time_by_milestone(self):
#         self.add_card_to_board(self.cards_locators.CYCLE_TIME_BY_MILESTONE, "Cycle time by Milestone Report card")
#
#     # Engagement reports--------------------------------------------------------------
#
#
# class EngCards(BasePage):
#     header_locators = HeaderLocators()
#     create_delete_board_locators = CreateDeleteBoards()
#     cards_locators = ReportCards()
#
#     def navigate_to_board(self):
#         try:
#             self.element_is_visible(self.header_locators.HEADER_BOARDS).click()
#             self.element_is_visible(self.create_delete_board_locators.BOARD_AUTOTEST).click()
#         except NoSuchElementException:
#             logging.error("AUTOTEST board is not accessible.")
#             raise
#
#     def add_engagement_report_card(self, report_type_locator, report_name):
#         self.element_is_visible(self.cards_locators.BOARDS_ADD_DROPDOWN).click()
#         self.element_is_visible(self.cards_locators.ADD_REPORT_CARD).click()
#         self.element_is_visible(self.cards_locators.ENGAGEMENT).click()
#         self.element_is_visible(report_type_locator).click()  # Select the specific report type
#         self.element_is_visible(self.cards_locators.REPORT_CARD_NAME).send_keys(report_name)
#         self.element_is_visible(self.cards_locators.REPORT_CARD_ADD).click()  # Click on the 'Add Report Card' button
#
#     def add_engagement_card_to_board(self, report_type_locator, report_name):
#         self.navigate_to_board()
#         self.add_engagement_report_card(report_type_locator, report_name)
#
#     def add_user_engagement_summary_report_card(self):
#         self.add_engagement_card_to_board(self.cards_locators.USER_ENGAGEMENT_SUMMARY, "User Engagement Summary")
#
#     def add_user_participation_summary_report_card(self):
#         self.add_engagement_card_to_board(self.cards_locators.USER_PARTICIPATION_SUMMARY,
#                                           "User Participation Summary Report card")
#
#     def add_engagement_by_location_report_card(self):
#         self.add_engagement_card_to_board(self.cards_locators.ENGAGEMENT_BY_LOCATION,
#                                           "Engagement by Location Report card")
#
#     def add_engagement_by_persona(self):
#         self.add_engagement_card_to_board(self.cards_locators.ENGAGEMENT_BY_PERSONA,
#                                           "Engagement by Persona Report card")
#
#
# class ImpactReportCards(BasePage):
#     header_locators = HeaderLocators()
#     create_delete_board_locators = CreateDeleteBoards()
#     cards_locators = ReportCards()
#
#     def navigate_to_board2(self):
#         try:
#             self.element_is_visible(self.header_locators.HEADER_BOARDS).click()
#             self.element_is_visible(self.create_delete_board_locators.BOARD_REPORT_CARDS2).click()
#         except NoSuchElementException:
#             logging.error("board is not accessible.")
#             raise
#
#     def add_impact_report_card(self, report_type_locator, report_name):
#         self.element_is_visible(self.cards_locators.BOARDS_ADD_DROPDOWN).click()
#         self.element_is_visible(self.cards_locators.ADD_REPORT_CARD).click()
#         self.element_is_visible(self.cards_locators.IMPACT).click()
#         self.element_is_visible(report_type_locator).click()  # Select the specific report type
#         self.element_is_visible(self.cards_locators.REPORT_CARD_NAME).send_keys(report_name)
#         self.element_is_visible(self.cards_locators.REPORT_CARD_ADD).click()  # Click on the 'Add Report Card' button
#
#     def add_impact_report_card_to_board(self, report_type_locator, report_name):
#         self.navigate_to_board2()
#         self.add_impact_report_card(report_type_locator, report_name)
#
#     def add_impact_summary_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.IMPACT_SUMMARY,
#                                              "Impact Summary Report card")
#
#     def add_impact_over_time_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.IMPACT_OVER_TIME,
#                                              "Impact Over Time Report card")
#
#     def add_impact_by_person_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.IMPACT_BY_PERSON,
#                                              "Impact by Person Report card")
#
#     def add_impact_by_location(self):
#         self.add_impact_report_card_to_board(self.cards_locators.IMPACT_BY_LOCATION,
#                                              "Impact by Location Report card")
#
#     def add_impact_by_item_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.IMPACT_BY_ITEM,
#                                              "Impact by Item Report card")
#
#     def add_impact_by_impact_value_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.IMPACT_BY_IMPACT_VALUE,
#                                              "Impact by Impact Value Report card")
#
#     def add_impact_by_milestone_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.IMPACT_BY_MILESTONE,
#                                              "Impact by Milestone Report card")
#
#
# class AttributeReportCards(BasePage):
#     header_locators = HeaderLocators()
#     create_delete_board_locators = CreateDeleteBoards()
#     cards_locators = ReportCards()
#
#     def navigate_to_board2(self):
#         try:
#             self.element_is_visible(self.header_locators.HEADER_BOARDS).click()
#             self.element_is_visible(self.create_delete_board_locators.BOARD_REPORT_CARDS2).click()
#         except NoSuchElementException:
#             logging.error("board is not accessible.")
#             raise
#
#     def add_impact_report_card(self, report_type_locator, report_name):
#         self.element_is_visible(self.cards_locators.BOARDS_ADD_DROPDOWN).click()
#         self.element_is_visible(self.cards_locators.ADD_REPORT_CARD).click()
#         self.element_is_visible(self.cards_locators.ATTRIBUTE).click()
#         self.element_is_visible(report_type_locator).click()  # Select the specific report type
#         self.element_is_visible(self.cards_locators.REPORT_CARD_NAME).send_keys(report_name)
#         self.element_is_visible(self.cards_locators.REPORT_CARD_ADD).click()  # Click on the 'Add Report Card' button
#
#     def add_impact_report_card_to_board(self, report_type_locator, report_name):
#         self.navigate_to_board2()
#         self.add_impact_report_card(report_type_locator, report_name)
#
#     def add_attribute_summary_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.ATTRIBUTE_SUMMARY,
#                                              "Attribute Summary Report card")
#
#     def add_activity_by_attribute_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.ACTIVITY_BY_ATTRIBUTE,
#                                              "Activity by Attribute Report card")
#
#     def add_impact_by_attribute_report_card(self):
#         self.add_impact_report_card_to_board(self.cards_locators.IMPACT_BY_ATTRIBUTE,
#                                              "Impact by Attribute Report card")
