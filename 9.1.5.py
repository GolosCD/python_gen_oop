import re

class DomainException(Exception):
    pass
    
class Domain:
    pattern_domain = r'\w+\.{1}\w{1,4}$'
    pattern_email = r''
    def __init__(self,text):
        self._domain = self.domain(text)
        
    @classmethod
    def check_dig(cls,text):
        check = re.search(r'\d+',text)
        if check:
            raise DomainException ('Недопустимый домен, url или email')
        
    def domain(self,text):
        self.check_dig(text)
        check = re.search(Domain.pattern_domain,text,re.M)
        if not check or text.count('.')>1:
            raise DomainException ('Недопустимый домен, url или email')
        return text
            
    def __str__(self):
        return self._domain
        
    @classmethod    
    def from_url(cls,text_in):
        cls.check_dig(text_in)
        if text_in.startswith('http://') or text_in.startswith('https://') and text_in.count(':')==1 and text_in.count('.')==1:
            check = re.search(cls.pattern_domain,text_in,re.M)
            if check and not text_in.endswith('/') and not '///' in text_in:
                return Domain(check.group(0))
            else:
                raise DomainException ('Недопустимый домен, url или email') 
        raise DomainException ('Недопустимый домен, url или email')         
           
    @classmethod    
    def from_email(cls,text_email):
        cls.check_dig(text_email)
        if '@' in text_email: 
            check = re.search(cls.pattern_domain,text_email,re.M)
            if check and text_email.count('@')==1 and not text_email.startswith('@'):
                return Domain(check.group(0))
            else:
                raise DomainException ('Недопустимый домен, url или email')            
        
urls = ['http://evseeva.info/', 'https:://ip.com/', 'https://www.ao.ru', 'https:///ip.ru', 'https://zao.',
        'https://.edu', 'http://oao.edu/', 'http://www.ip.com/', 'http://.org', 'http://abc.']

for url in urls:
    try:
        domain = Domain.from_url(url)
        print(domain,url,url.count(':'))
    except DomainException as e:
        print(e)