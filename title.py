from geometor.utils import *
from geometor.model import *
from geometor.title import *

sp.init_printing()

#  title = input(f'\ntitle: ')


title = f'G E O M E T O R'
f = plot_title(title, 'title', 'geometor.png', color='#cc9900', size=60)
print(f)
plt.show()
f = plot_title('Hello World!', 'title', 'hello.png')
print(f)
plt.show()
