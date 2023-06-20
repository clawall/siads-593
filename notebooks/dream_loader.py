import json
import pandas as pd
import re

# This regex pattern creates groups from the Dataset file names and allows us to create new columns
dream_filename_pattern = re.compile(r'^(?P<discard>.\/assets\/DREAMdataset\/User\s\d+\/User\s)(?P<user_id>\d+)\_(?P<index>\d+)\_(?P<step>[a-zA-Z]+|[a-zA-Z]+\s[a-zA-Z]+|[a-zA-Z]+\s\d+\s*[a-zA-Z]{0,1})\_(?P<date>\d+)\_(?P<time>\d+)')
dream_pattern_group_indexes = dream_filename_pattern.groupindex


def item_or_default(array, index, default_value=None):
    """
    Gets an item from the array at the specified index and returns a default_value if none exist.
    """
    try:
        return array[index]
    except IndexError:
        return default_value

def normalize_dream_json(filename, split_gaze=False):
    """
    Reads the JSON file and normalizes it to an array, allowing the gazes to be added as new rows if indicated.
    """
    with open(filename) as json_file:
        re_result = re.search(dream_filename_pattern, filename)
        
        contents = json.load(json_file)

        user_id = re_result.group(dream_pattern_group_indexes.get('user_id'))
        file_index = re_result.group(dream_pattern_group_indexes.get('index'))
        evaluation_step = re_result.group(dream_pattern_group_indexes.get('step'))
        date = re_result.group(dream_pattern_group_indexes.get('date'))
        time = re_result.group(dream_pattern_group_indexes.get('time'))
        
        pre_test = {f'preTest.{k}': v for k, v in contents.get('ados', {}).get('preTest', {}).items()}
        post_test = {f'postTest.{k}': v for k, v in contents.get('ados', {}).get('postTest', {}).items()}
        participant = contents.get('participant')
        frame_rate = contents.get('frame_rate')
        condition = contents.get('condition')
        task = {f'task.{k}': v for k, v in contents.get('task', {}).items()}
        eye_gaze = contents.get('eye_gaze')
        head_gaze = contents.get('head_gaze')

        metadata = {
            'user_id': user_id,
            'file_index': file_index,
            'evaluation_step': evaluation_step,
            'date': date,
            'time': time,
            'frame_rate': frame_rate,
            'condition': condition,
            **pre_test, **post_test, **participant, **task
        }

        if split_gaze:
            length = max(len(eye_gaze['rx']), len(eye_gaze['ry']), len(eye_gaze['rz']), len(head_gaze['rx']), len(head_gaze['ry']), len(head_gaze['rz']))
            
            current_data = []
            
            for i in range(0, length):
                current_data.append({
                    **metadata,
                    'gaze_index': i,
                    'eye_gaze_rx': item_or_default(eye_gaze['rx'], i),
                    'eye_gaze_ry': item_or_default(eye_gaze['ry'], i),
                    'eye_gaze_rz': item_or_default(eye_gaze['rz'], i),
                    'head_gaze_rx': item_or_default(head_gaze['rx'], i),
                    'head_gaze_ry': item_or_default(head_gaze['ry'], i),
                    'head_gaze_rz': item_or_default(head_gaze['rz'], i)
                })

            return current_data
        
        return [metadata]

