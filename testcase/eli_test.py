import unittest

from time import sleep

import uiautomator2 as u2

from utils.getyaml import yl


class eli_login(unittest.TestCase):
    def setUp(self):
        
        self.dl = u2.connect(yl['setup']['devices'])
        #print(self.dl.device_info)
        self.dl.app_start(yl['setup']['page'])

    def tearDown(self):
        self.dl.app_stop(yl['setup']['page'])
    def test_login_login(self):
        #self.dl(id='cn.eliteu.android:id/email_et').set_text('13226349780')
        self.dl(text=u'跳过').click()
        self.dl(className = 'android.widget.ImageButton').click_exists(timeout=10)

        sleep(5)




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(eli_login)
    unittest.TextTestRunner(verbosity=2).run(suite)