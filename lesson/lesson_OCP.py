'''
Этот файл - повторение материала урока по
Принципу открытости/закрытости (OCP, Open/Closed Principle)

✅Программные сущности (классы, модули, функции и т.д.)
должны быть открыты для расширения, но закрыты для модификации.
Суть в том, что уже существующий код не должен модифицироваться
при добавлении новых функций. Это достигается за счёт
использования абстракций и интерфейсов.
Другими словами, должна быть возможность добавлять новый функционал
в программу, но при этом не изменять уже существующий код.
'''

# Абстрактный класс - шаблон для других классов
from abc import ABC, abstractmethod


class Formatted(ABC):
    @abstractmethod
    def format(self,  report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f'<h1>{report.title}</h1>')
        print(f'<p>{report.content}</p>')

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def doc_printer(self):
        self.formatted.format(self)

report_text = Report('Заголовок', 'Текст отчета, его тут много', TextFormatted())
report_text.doc_printer()
print()
report_html = Report('Заголовок html', 'Текст отчета html', HtmlFormatted())
report_html.doc_printer()