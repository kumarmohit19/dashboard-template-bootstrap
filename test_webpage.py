from bs4 import BeautifulSoup
import pytest
import pickle
import requests

class TestWebpage:
    @pytest.fixture(autouse=True)
    def get_soup(self):
        index_page = requests.get("http://localhost:8000/index.html")
        soup_index = BeautifulSoup(index_page.content, 'html.parser')
        self._index = soup_index
        action_page = requests.get("http://localhost:8000/action.html")
        soup_action = BeautifulSoup(action_page.content, 'html.parser')
        self._action = soup_action
       
    # testing index.html
    def test_index_nav(self):
        assert self._index.find_all('nav')
    def test_index_navbar(self):
        assert self._index.find('a',{'class':'navbar-brand'})
        assert self._index.find('button',{'data-target':'#navbarCollapse'})
        assert self._index.find('div',{'class':'navbar-header'})
    def test_index_page(self):
        assert self._index.find('form',{'class':'navbar-form navbar-right'})
        assert self._index.find('button',{'class':'btn btn-default'})
        assert self._index.find('span',{'class':'glyphicon glyphicon-search'})
        assert self._index.find('div',{'class':'navbar-primary sidebar'})  
        assert self._index.find('div',{'class':'row'})  
        assert self._index.find('div',{'class':'col-lg-3'})  
        assert self._index.find('div',{'class':'col-lg-8'}) 
        a=0
        for li in self._index.find_all('li'):
            a=a+1
        assert a==6 
        site =  self._index.find('div',{'class':'panel panel-default'})
        b=0
        for site in self._index.find_all('div',{'class':'panel panel-default'}):
            b=b+1
        assert b>=4
        site1 =  self._index.find('div',{'class':'panel-body'})
        c=0
        for site1 in self._index.find_all('div',{'class':'panel-body'}):
            c=c+1
        assert c>=4
        d=0
        for img in self._index.find_all('img'):
            d=d+1
        assert d>=4
#action.html--------------------------------------------------------------------
    def test_action_nav(self):
        assert self._action.find_all('nav')
    def test_index_navbar(self):
        assert self._action.find('a',{'class':'navbar-brand'})
        assert self._action.find('button',{'data-target':'#navbarCollapse'})
        assert self._action.find('div',{'class':'navbar-header'})
    def test_row(self):
        assert self._action.find('form',{'class':'navbar-form navbar-right'})
        assert self._action.find('button',{'class':'btn btn-default'})
        assert self._action.find('span',{'class':'glyphicon glyphicon-search'})
        assert self._action.find('div',{'class':'navbar-primary sidebar'})  
        assert self._action.find('div',{'class':'row'})  
        assert self._action.find('div',{'class':'col-lg-3'})  
        assert self._action.find('div',{'class':'col-lg-9'}) 
        a=0
        for li in self._action.find_all('li'):
            a=a+1
        assert a==6 
    def test_centre_page(self):
        site=self._action.find('div',{'class':'col-lg-3'})
        a=0
        for site in self._action.find_all('div',{'class':'col-lg-3'}):
            a=a+1
        assert a>=6
        b=0
        for img in self._action.find_all('img'):
            b=b+1
        assert b>=6
        c=0
        for button in self._action.find_all('button'):
            c=c+1
        assert c>=6
