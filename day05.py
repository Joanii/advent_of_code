import numpy as np
import yaml
from day05_input import *


def translate(input, map, type='', return_margin=False):
    source_idx = 1
    destination_idx = 0
    range_idx = 2
    diff = input - map[:, source_idx]
    diff[diff < 0] = diff.max()
    if (diff < 0).any():
        print('error')
    line_index = diff.argmin()
    offset = diff[line_index]
    if offset >= map[line_index, range_idx]:
        output = input
    else:
        output = map[line_index, destination_idx] + offset
    margin = map[line_index, range_idx] - offset
    if return_margin:
        return output, margin
    else:
        return output


def location_from_seed(seeds):
    locations = []
    for seed in seeds:
        soil = translate(seed, seed_to_soil, type='soil')
        fertilizer = translate(soil, np.array(soil_to_fertilizer), type='fertilizer')
        water = translate(fertilizer, np.array(fertilizer_to_water), type='water')
        light = translate(water, np.array(water_to_light), type='light')
        temperature = translate(light, np.array(light_to_temperature), type='light')
        humidity = translate(temperature, np.array(temperature_to_humidity), type='temperature')
        location = translate(humidity, np.array(humidity_to_location), type='location')
        locations.append(location)
    min_location = np.array(locations).min()
    print(min_location)
    return min_location


if __name__ == '__main__':
    input_seeds = [364807853, 408612163, 302918330, 20208251, 1499552892, 200291842, 3284226943, 16030044, 2593569946,
                   345762334, 3692780593, 17215731, 1207118682, 189983080, 2231594291, 72205975, 3817565407, 443061598,
                   2313976854, 203929368]
    # Task 1
    # location_from_seed(input_seeds)

    # Task 2
    input_seeds = np.array(input_seeds).reshape(-1, 2)
    locations = []
    for seed_range in input_seeds:
        seed = seed_range[0]
        while seed < seed_range[0] + seed_range[1]:
            margins = []
            soil, margin = translate(seed, seed_to_soil, type='soil', return_margin=True)
            margins.append(margin)
            fertilizer, margin = translate(soil, np.array(soil_to_fertilizer), type='fertilizer', return_margin=True)
            margins.append(margin)
            water, margin = translate(fertilizer, np.array(fertilizer_to_water), type='water', return_margin=True)
            margins.append(margin)
            light, margin = translate(water, np.array(water_to_light), type='light', return_margin=True)
            margins.append(margin)
            temperature, margin = translate(light, np.array(light_to_temperature), type='light', return_margin=True)
            margins.append(margin)
            humidity, margin = translate(temperature, np.array(temperature_to_humidity), type='temperature', return_margin=True)
            margins.append(margin)
            location, margin = translate(humidity, np.array(humidity_to_location), type='location', return_margin=True)
            margins.append(margin)
            min_margin = min(margins)
            if min_margin > 0:
                seed = seed + min_margin - 1
            else:
                seed += 1
            locations.append(location)
    print(min(locations))
