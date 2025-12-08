import xml.etree.ElementTree as ET
from typing import List, Dict, Any

def load_users_data(file_path: str = "users.xml"):
    users = []
    tree = ET.parse(file_path)
    root = tree.getroot()
        
    for user_elem in root.findall('user'):
        user = {
            'user_id': int(user_elem.find('user_id').text),
            'name': user_elem.find('name').text,
            'age': int(user_elem.find('age').text),
            'weight': float(user_elem.find('weight').text),
            'fitness_level': user_elem.find('fitness_level').text
        }
        users.append(user)
    
    return users

def load_workouts_data(file_path: str = "workout.xml"):
    workouts = []
    tree = ET.parse(file_path)
    root = tree.getroot()
        
    for workout_elem in root.findall('workout'):
        workout = {
            'workout_id': int(workout_elem.find('workout_id').text),
            'user_id': int(workout_elem.find('user_id').text),
            'date': workout_elem.find('date').text,
            'type': workout_elem.find('type').text,
            'duration': int(workout_elem.find('duration').text),
            'distance': float(workout_elem.find('distance').text),
            'calories': int(workout_elem.find('calories').text),
            'avg_heart_rate': int(workout_elem.find('avg_heart_rate').text),
            'intensity': workout_elem.find('intensity').text
            }
        workouts.append(workout)
    
    return workouts

def get_stats(users: List[Dict[str, Any]], workouts: List[Dict[str, Any]]):
    if not workouts:
        return {}
    
    stats = {
        'total_workouts': len(workouts),
        'total_users': len(set(w['user_id'] for w in workouts)),
        'total_duration_minutes': sum(w['duration'] for w in workouts),
        'total_distance_km': sum(w['distance'] for w in workouts),
        'total_calories': sum(w['calories'] for w in workouts),
        'avg_duration': 0,
        'avg_distance': 0,
        'avg_calories': 0,
        'avg_heart_rate': 0,
        'workouts_by_type': {},
        'workouts_by_intensity': {},
        'workouts_by_user': {}
    }
    
    stats['avg_duration'] = stats['total_duration_minutes'] / stats['total_workouts']
    stats['avg_distance'] = stats['total_distance_km'] / stats['total_workouts']
    stats['avg_calories'] = stats['total_calories'] / stats['total_workouts']
    stats['avg_heart_rate'] = sum(w['avg_heart_rate'] for w in workouts) / stats['total_workouts']
    

    for workout in workouts:
        workout_type = workout['type']
        stats['workouts_by_type'][workout_type] = stats['workouts_by_type'].get(workout_type, 0) + 1
        
        intensity = workout['intensity']
        stats['workouts_by_intensity'][intensity] = stats['workouts_by_intensity'].get(intensity, 0) + 1
        
        user_id = workout['user_id']
        stats['workouts_by_user'][user_id] = stats['workouts_by_user'].get(user_id, 0) + 1
    
    return stats

def main():
    users = load_users_data()
    workouts = load_workouts_data()
    
    print("Загружено пользователей:", len(users))
    print("Загружено тренировок:", len(workouts))
    
    stats = get_stats(users, workouts)
    

print("\n=== ОБЩАЯ СТАТИСТИКА ПО ТРЕНИРОВКАМ ===")
    print(f"Всего тренировок: {stats.get('total_workouts', 0)}")
    print(f"Всего уникальных пользователей: {stats.get('total_users', 0)}")
    print(f"Общая продолжительность: {stats.get('total_duration_minutes', 0)} минут")
    print(f"Общая дистанция: {stats.get('total_distance_km', 0):.2f} км")
    print(f"Всего сожжено калорий: {stats.get('total_calories', 0)}")
    print(f"Средняя продолжительность: {stats.get('avg_duration', 0):.2f} минут")
    print(f"Средняя дистанция: {stats.get('avg_distance', 0):.2f} км")
    print(f"Среднее количество калорий: {stats.get('avg_calories', 0):.2f}")
    print(f"Средний пульс: {stats.get('avg_heart_rate', 0):.2f}")
    
    print("\n=== ТРЕНИРОВКИ ПО ТИПАМ ===")
    for workout_type, count in stats.get('workouts_by_type', {}).items():
        print(f"{workout_type}: {count}")
    
    print("\n=== ТРЕНИРОВКИ ПО ИНТЕНСИВНОСТИ ===")
    for intensity, count in stats.get('workouts_by_intensity', {}).items():
        print(f"{intensity}: {count}")
    
    print("\n=== ТРЕНИРОВКИ ПО ПОЛЬЗОВАТЕЛЯМ ===")
    for user_id, count in stats.get('workouts_by_user', {}).items():
        print(f"Пользователь {user_id}: {count} тренировок")

if name == "__main__":
    main()