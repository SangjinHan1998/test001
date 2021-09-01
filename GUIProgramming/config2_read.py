from configparser import ConfigParser, ExtendedInterpolation

parser = ConfigParser(interpolation=ExtendedInterpolation())
parser.read('dev.ini')      # 파서(문장의 구조 분석·오류 점검 프로그램)

print(parser.sections())
print(parser.get('settings', 'secret_key'))
print(parser.options('settings'))

print('db' in parser)   # 섹션이 파일에 있는가? 
print(parser.get('db','db_port'), type(parser.get('db', 'db_port')))
print(int(parser.get('db','db_port')))
print(parser.getint('db', 'db_port'))
print(parser.getint('db', 'db_default_port', fallback = 3306))

print(parser.getboolean('settings', 'debug'))

print(parser.get('files', 'python_path'))
