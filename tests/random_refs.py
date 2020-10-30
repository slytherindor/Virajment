import uuid

def random_suffix():
    return uuid.uuid4().hex[:6]

def random_building_id(name=''):
    return f'bldng-{name}-{random_suffix()}'

def random_building_section(name=''):
    return f'bldng-section-{name}-{random_suffix()}'

def random_location(name=''):
    return f'lctn-{name}-{random_suffix()}'
