from pathlib import Path

# the destination range start, the source range start, and the range length.


def readFile(inputPath: str):
    (_, seeds, *rest) = list(filter(None, Path(inputPath).read_text().splitlines()))
    return (_, seeds, rest)


def initial_seeds(seeds_from_text: str):
    return [int(x) for x in seeds_from_text.split(" ")]


def seeds_range_part2(seeds_from_text: str):
    seeds_individual = initial_seeds(seeds_from_text)
    acc = []
    for seed, gen_range in zip(seeds_individual[::2], seeds_individual[1::2]):
        l = list(range(seed, seed + gen_range))
        acc.extend(l)
    return acc


# test = "5844012 110899473 1132285750 58870036 986162929 109080640 3089574276 100113624 2693179996 275745330 2090752257 201704169 502075018 396653347 1540050181 277513792 1921754120 26668991 3836386950 66795009"
# print(seeds_range_part2(test))


def solution_part1():
    (_, seeds_str, rest) = readFile("day5/in.txt")

    # seeds = initial_seeds(seeds_str)
    seeds = seeds_range_part2(seeds_str)

    (
        seed_to_soil_index,
        soil_to_fert_index,
        fert_to_water_index,
        water_to_light_index,
        light_to_temp_index,
        temp_to_hum_index,
        hum_to_loc_index,
    ) = (
        rest.index(category)
        for category in (
            "seed-to-soil map:",
            "soil-to-fertilizer map:",
            "fertilizer-to-water map:",
            "water-to-light map:",
            "light-to-temperature map:",
            "temperature-to-humidity map:",
            "humidity-to-location map:",
        )
    )

    seed_to_soil = rest[seed_to_soil_index + 1 : soil_to_fert_index]
    soil_to_fert = rest[soil_to_fert_index + 1 : fert_to_water_index]
    fert_to_water = rest[fert_to_water_index + 1 : water_to_light_index]
    water_to_light = rest[water_to_light_index + 1 : light_to_temp_index]
    light_to_temp = rest[light_to_temp_index + 1 : temp_to_hum_index]
    temp_to_hum = rest[temp_to_hum_index + 1 : hum_to_loc_index]
    hum_to_loc = rest[hum_to_loc_index + 1 :]

    all_values = [
        seed_to_soil,
        soil_to_fert,
        fert_to_water,
        water_to_light,
        light_to_temp,
        temp_to_hum,
        hum_to_loc,
    ]

    a, b, c, d, e, f, g = list(map(lambda x: convert_list_into_ranges(x), all_values))

    interm_a = collect_seeds_after_conversion(a, seeds)
    interm_b = collect_seeds_after_conversion(b, interm_a)
    interm_c = collect_seeds_after_conversion(c, interm_b)
    interm_d = collect_seeds_after_conversion(d, interm_c)
    interm_e = collect_seeds_after_conversion(e, interm_d)
    interm_f = collect_seeds_after_conversion(f, interm_e)
    interm_g = collect_seeds_after_conversion(g, interm_f)

    # 825516882 correct
    return min(interm_g)


def collect_seeds_after_conversion(coords: list[tuple], input: list[int]):
    acc = []
    match = False
    for seed in input:
        # print(seed)
        match = False
        for src_start, src_end, dest_start, dest_end in coords:
            if src_start <= seed <= src_end:
                # print(
                #     "seed is",
                #     seed,
                #     "between",
                #     src_start,
                #     "and",
                #     src_end,
                #     "corr to",
                #     dest_start,
                #     "-",
                #     dest_end,
                # )
                acc.append(dest_start + (seed - src_start))
                match = True
        if not match:
            # print("using current number as no match", seed)
            acc.append(seed)

    return acc


def convert_list_into_ranges(vals: list[str]):
    vals_converted = []

    for val in vals:
        dest_start, src_start, gen_range = [int(x) for x in val.split(" ")]
        vals_converted.append(
            (
                src_start,
                src_start + gen_range - 1,
                dest_start,
                dest_start + gen_range - 1,
            )
        )
    return vals_converted


print(solution_part1())
