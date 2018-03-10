import unittest

from time import sleep

import uiautomator2 as u2

from utils.getyaml import yl


class eli_login(unittest.TestCase):
    def setUp(self):
        self.dl = u2.connect(yl['setup']['devices'])
        #print(self.dl.device_info)
        self.dl.app_clear(yl['setup']['page'])
        #清除数据，=重新装一次
        self.dl.app_start(yl['setup']['page'])

    def tearDown(self):
        self.dl.app_stop(yl['setup']['page'])
    def test_1login_login(self):
        self.dl.set_fastinput_ime(True)
        self.dl(resourceId=yl['login_t']['un_input']).set_text('13226349780')
        self.dl(resourceId=yl['login_t']['password']).click_exists(timeout=3)
        self.dl(resourceId=yl['login_t']['password']).set_text('19940919')
        #self.dl(text='密码').set_text('19940919')
        #self.dl(text='跳过').click()
        #self.dl(className = yl['login_t']['nav']).click_exists(timeout=10)
        self.dl(resourceId = yl['login_t']['login']).click_exists(timeout=3)
        ac = self.dl.current_app()
        acq = ac['activity'].split('.')
        #print(acq[-1])
        assert (acq[-1] == yl['login_t']['la'])

    def test_2_ls(self):
        self.dl(resourceId = yl['test_ls']['skip']).click_exists(timeout=3)
        self.dl(className = yl['test_ls']['nav']).click_exists(timeout=3)
        self.dl(resourceId = yl['test_ls']['login_btn']).click_exists(timeout=3)
        ac = self.dl.current_app()
        acq = ac['activity'].split('.')
        #print(acq[-1])
        assert (acq[-1] == yl['test_ls']['la'])

    def test_3_login_skip(self):
        self.dl(resourceId=yl['test_lk']['skip']).click_exists(timeout=3)
        self.dl(resourceId=yl['test_lk']['select']).click_exists(timeout=3)
        course = self.dl(className = yl['test_lk']['courses'])
        print(course[1])
        course[1].click()
        self.dl.swipe(579,1500,579,800,0.5)
        self.dl(resourceId = yl['test_lk']['join']).click()
        ac = self.dl.current_app()
        acq = ac['activity'].split('.')
        # print(acq[-1])
        assert (acq[-1] == yl['test_lk']['la'])



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(eli_login)
    unittest.TextTestRunner(verbosity=2).run(suite)