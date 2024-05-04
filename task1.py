from pathlib import Path
import shutil

        
def dir_copy(source_path, destination_path=None):
# перевіряємо чи існує джерело    
    if not source_path.exists():
        print('Origin path doesn`t exist')
        return
    
# перевіряємо, чи передана тека призначення, якщо ні, то формуємо її назву за замовчуванням   
    if not destination_path:
        destination_path = source_path.parent / "dist"
        destination_path = Path(destination_path)
        
# перевіряємо чи існує тека призанчення. Якщо ні, то створюємо   
    if not destination_path.exists():
        try:
            destination_path.mkdir(parents=True, exist_ok=True)
        except Exception as error:
            print('Failed to create to_path')
            return

# функція копіювання (рекурсивна)
    def copying(source, dist):
        for child in source.iterdir():

# якщо єлемент є текою, то лише запускаємо рекурсію            
            if child.is_dir():
                copying(child, dist)
                continue

# якщо елемент є файлом, створюємо теку з назвою його розширення            
            file_extension = child.suffix.replace('.', '') or 'no_name'
            dir_name = Path(f"{dist}\{file_extension}")
            dir_name.mkdir(parents=True, exist_ok=True)

# фомруємо новий шлях для файла            
            new_file_name = Path(f"{dir_name}\{child.name}")    
                    
            print(new_file_name)
            
# копіюємо, обробляючи можливі виключення           
            try:
                shutil.copy2(child, new_file_name)
            except Exception:
                print('Failed to copy ', child.name)
                
    copying(source_path, destination_path)
    
    
dir_copy(Path('C:/Projects Magistr'), Path("C:/Projects Magistr1"))
    
    