Early Access version. 
===============
Эта версия - staging-вариант интерфейса управления программно-определяемой сетью для проекта zVirt. 

Ведутся работы по включению в основной репозиторий проекта. 

Инструкция по установке:
1) git clone https://github.com/su30sm/zv-ovn-client

2) cd zv-ovn-client 

3) pip install -e .

Инструкция по применению:
1) Следующие переменные окружения задают конфигурацию утилиты. В случае, если переменная с паролем не задана - пароль будет запрошен интерактивно.

export OS_USERNAME=admin@internal

export OS_PASSWORD='Ваш_Пароль'

export OS_AUTH_URL=https://localhost:35357/v2.0

export OS_CACERT=/etc/pki/ovirt-engine/ca.pem

2) Для поддержки всех актуальных версий (помимо тестируемых) рекомендуется применять ключ  --insecure при использовании утилиты openstack. 

Рекомендуется сформировать псевдоним, например alias openstack="openstack --insecure"

3) openstack [--insecure] network list  для проверки подключения. 
