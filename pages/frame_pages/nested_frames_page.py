from playwright.sync_api import Page
from framework.ui.elements.label import Label
from framework.ui.pages.base_page import BasePage

class NestedFramesPage(BasePage):
    def __init__(self, page: Page):
        unique_element = Label(page, page.locator('frame[name="frame-top"]'), "unique element of Nested Frames Page")
        super().__init__(page, unique_element, 'Nested Frames Page')
        
        self._left_frame_label = Label(
            page, 
            page.frame_locator('frame[name="frame-top"]').frame_locator('frame[name="frame-left"]').locator('body'), 
            'Left Frame label'
        )
        # Implement right frame
        
    # Implement methods
