import time
from _pydatetime import timedelta
from datetime import datetime, timezone
from locators.HEADER_LOCATORS.header_page_locators import HeaderLocators, CreateBtnItemsDropdown, CreateDeleteBoards, \
    CreateDeleteBoards, ReportCards
from locators.ITEM_CREATE_WINDOW_LOCATORS.item_create_window_locators import ItemCreateWindow
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage
import logging


class CreateAdvancedItem(BasePage):
    header_locators = HeaderLocators()
    create_btn_locators = CreateBtnItemsDropdown()
    locators = ItemCreateWindow()

    # def future_timestamp(self, days=6):
    #      current_utc_time = datetime.now(timezone.utc)
    #      future_utc_time = current_utc_time + timedelta(days=days)
    #      formatted_future_time = future_utc_time.utctime("%Y, %b %d %I:%M %p")
    #      return formatted_future_time
    #
    #  def current_timestamp(self):
    #      current_time = datetime.now()
    #      formatted_time = current_time.strftime("%Y, %b %d %-I:%M %p")
    #      return formatted_time


