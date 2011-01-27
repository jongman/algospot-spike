# 개발 시작하기

1. 먼저 git repository 를 클론한다.

	$ git clone git@github.com:jongman/algospot-spike.git
	$ cd algospot-spike

1. 사이트에 필요한 각종 패키지들을 깔기 위해 easy\_install 을 깔고, easy\_install 로 pip 을 깐다. easy\_install 이랑 pip 은 둘다 파이썬 패키지 매니저인데, pip 이 더 최신이지만 아직 우분투 리포지토리에 안 들어가 있다. easy\_install 은 처음에 pip 까는 용도 빼고는 쓰지 않는다.

	$ sudo apt-get install python-setuptools
	...
	$ sudo easy_install pip

1. virtualenv 를 깐다. virtualenv 는 파이썬 패키지를 로컬 디렉토리에 깔 수 있게 해 주는 도구다. 시스템 전역에 깔지 않아도 되기 때문에 두 개 이상의 프로젝트의 dependency 가 충돌하거나 할 일이 없음. virtualenv 가 진리임. ㅇㅇ

	$ sudo pip install virtualenv

1. virtualenv 환경을 만들고 activate 한다. 이후 까는 모든 패키지는 env 디렉토리 내에 깔리게 되며, sudo 권한 없이도 깔 수 있다.

	$ virtualenv env
	$ source env/bin/activate

1. algospot 사이트에 필요한 각종 파이썬 패키지는 requirements.txt 에 들어있다. pip 을 이용해 requirements 에 들어 있는 패키지들을 깐다. 이렇게 하면 django 랑 기타 장고 앱들을 다 깔아 준다.

	$ pip install -r requirements.txt

1. 투비컨티뉴드 ..
