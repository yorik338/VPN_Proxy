import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, \
    QPushButton, QVBoxLayout, QMessageBox


class ProxyToVPNApp(QWidget):
    def __init__(self):
        super().__init__()

        # Настраиваем интерфейс
        self.init_ui()

    def init_ui(self):
        # Заголовок окна
        self.setWindowTitle('Proxy to VPN')

        # Виджеты для ввода данных
        self.proxy_label = QLabel('Введите прокси (в формате: адрес:порт):')
        self.proxy_input = QLineEdit()

        self.username_label = QLabel('Логин прокси (если требуется):')
        self.username_input = QLineEdit()

        self.password_label = QLabel('Пароль прокси (если требуется):')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Кнопка активации прокси
        self.activate_button = QPushButton('Активировать прокси')
        self.activate_button.clicked.connect(self.activate_proxy)

        # Размещение виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.proxy_label)
        layout.addWidget(self.proxy_input)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.activate_button)

        self.setLayout(layout)

    def activate_proxy(self):
        # Получаем данные прокси от пользователя
        proxy = self.proxy_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if proxy:
            try:
                # Пример команды для настройки proxychains
                # Здесь предполагается, что у вас установлен proxychains, и
                # вы его используете для перенаправления трафика
                config_path = os.path.expanduser(
                    '~/.proxychains/proxychains.conf')

                with open(config_path, 'a') as config_file:
                    if username and password:
                        config_file.write(
                            f'http {username}:{password}@{proxy}\n')
                    else:
                        config_file.write(f'http {proxy}\n')

                QMessageBox.information(self, 'Успех',
                                        'Прокси успешно активирован через proxychains!')
            except Exception as e:
                QMessageBox.critical(self, 'Ошибка',
                                     f'Не удалось активировать прокси: {str(e)}')
        else:
            QMessageBox.warning(self, 'Ошибка', 'Введите данные прокси.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProxyToVPNApp()
    window.show()
    sys.exit(app.exec_())
