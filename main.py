import costfunctions as cf
import dataexports as de

runs = 30
bounds = (-100, 100)
f_de_rand_1_bin = 0.8
cr_de_rand_1_bin = 0.9

f_de_best_1_bin = 0.5
cr_de_best_1_bin = 0.9

c1_pso = float(1.49618)
c2_pso = float(1.49618)
w_pso = float(0.7298)

path_length_soma = float(3)
step_size_soma = float(0.11)
prt_soma = float(0.7)

function_dictionary = {
    1: ("Rastrigin's function", cf.f1_rastrigins_function),
    2: ("Schwefel's function", cf.f2_schwefels_function),
    3: ("Griewank's function", cf.f3_griewanks_function),
    4: ("Sine envelope sine wave function", cf.f4_sine_envelope_sine_wave_function),
    5: ("Stretched V sine wave function", cf.f5_stretched_v_sine_wave_function),
    6: ("Ackley's function II", cf.f6_ackleys_function_ii),
    7: ("Egg holder function", cf.f7_egg_holder),
    8: ("Rana's function", cf.f8_ranas_function),
    9: ("Michalewicz's function", cf.f9_michalewiczs_function),
    10: ("Masters' cosine wave function", cf.f10_masters_cosine_wave_function),
    11: ("Bukin function N. 6", cf.f11_bukin_function_n_6),
    12: ("Cross-in-tray function", cf.f12_cross_in_tray_function),
    13: ("'Jednoduchá cosinová' function", cf.f13_jednoducha_cosinova),
    14: ("Holder table function", cf.f14_holder_table_function),
    15: ("'Ježatý bazének' function", cf.f15_jezaty_bazenek),
    16: ("'Lesoharmonika' function", cf.f16_lesoharmonika),
    17: ("'Kosmická loď' function", cf.f17_kosmicka_lod),
    18: ("'Místo dopadu' function", cf.f18_misto_dopadu),
    19: ("'Sopka' function", cf.f19_sopka),
    20: ("'Paralelní koryta' function", cf.f20_paralelni_koryta),
    21: ("'Vlnitý čtyřlístek' function", cf.f21_vlnity_ctyrlistek),
    22: ("'Duny s horami' function", cf.f22_duny_s_horami),
    23: ("'Fosílie' function", cf.f23_fosilie),
    24: ("'Vlnobití' function", cf.f24_vlnobiti),
    25: ("'Vlnité skluzavky' function", cf.f25_vlnite_skluzavky),
}

dimension = 30  # 2, 10, 30
population_size = 10 if dimension == 2 else 20 if dimension == 10 else 50

# DE_rand_1_bin
# dirname = "./output/DE_rand_1_bin/"
# for i in range(0, 25):
#     function_nbr = i + 1
#     filenamebase = f"DE_rand_1_bin_timeline_d{dimension}_f{function_nbr}"
#     titlebase = f"DE rand/1/bin on {function_dictionary[function_nbr][0]} with dimension {dimension}"
#
#     convergences = list()
#     final_results = list()
#     averages = list()
#
#     de.process_multiple_runs_de_rand_1_bin(runs, function_nbr, function_dictionary, dimension, population_size,
#                                            bounds, 2000 * dimension, f_de_rand_1_bin, cr_de_rand_1_bin, convergences,
#                                            final_results, averages,
#                                            dirname, filenamebase, titlebase, "")

# # DE_best_1_bin
# dirname = "./output/DE_best_1_bin/"
# for i in range(0, 25):
#     functionNbr = i + 1
#     filenamebase = f"DE_best_1_bin_timeline_d{dimension}_f{functionNbr}"
#     titlebase = f"DE best/1/bin on {function_dictionary[functionNbr][0]} with dimension {dimension}"
#
#     convergences = list()
#     final_results = list()
#     averages = list()
#
#     de.process_multiple_runs_de_best_1_bin(runs, functionNbr, function_dictionary, dimension, population_size,
#                                            bounds, 2000 * dimension, f_de_best_1_bin, cr_de_best_1_bin, convergences,
#                                            final_results, averages,
#                                            dirname, filenamebase, titlebase, "")

short_times = [range(0, 13), range(14, 18), range(19, 25)]
long_times = [range(13, 14), range(18, 19)]

# dirname = "./output/SOMA_all-to-one/"
# for st in short_times:
#     for i in st:
#         functionNbr = i + 1
#         filenamebase = f"SOMA_all-to-one_timeline_d{dimension}_f{functionNbr}"
#         titlebase = f"SOMA all-to-one on {function_dictionary[functionNbr][0]} with dimension {dimension}"
# 
#         convergences = list()
#         final_results = list()
#         averages = list()
# 
#         de.process_multiple_runs_soma_all_to_one(runs, functionNbr, function_dictionary, dimension, population_size,
#                                                  bounds, 2000 * dimension, path_length_soma, step_size_soma, prt_soma,
#                                                  convergences,
#                                                  final_results, averages,
#                                                  dirname, filenamebase, titlebase, "")

# # SOMA all-to-all
# dirname = "./output/SOMA_all-to-all/"
# for st in short_times:
#     for i in st:
#         functionNbr = i + 1
#         filenamebase = f"SOMA_all-to-all_timeline_d{dimension}_f{functionNbr}"
#         titlebase = f"SOMA all-to-all on {function_dictionary[functionNbr][0]} with dimension {dimension}"
#
#         convergences = list()
#         final_results = list()
#         averages = list()
#
#         de.process_multiple_runs_soma_all_to_all(runs, functionNbr, function_dictionary, dimension, population_size,
#                                                  bounds, 2000 * dimension, path_length_soma, step_size_soma, prt_soma,
#                                                  convergences,
#                                                  final_results, averages,
#                                                  dirname, filenamebase, titlebase, "")

# # PSO
# dirname = "./output/PSO/"
# for r in short_times:
#     for i in r:  # use 0 as first and 25 as last parameter to run all functions
#         functionNbr = i + 1
#         filenamebase = f"PSO_timeline_d{dimension}_f{functionNbr}"
#         titlebase = f"PSO on {function_dictionary[functionNbr][0]} with dimension {dimension}"
#
#         convergences = list()
#         final_results = list()
#         averages = list()
#
#         de.process_multiple_runs_pso(runs, functionNbr, function_dictionary, dimension, population_size,
#                                      bounds, 2000 * dimension, c1_pso, c2_pso, w_pso, convergences,
#                                      final_results, averages,
#                                      dirname, filenamebase, titlebase, "")
#
# for r in long_times:
#     for i in r:  # use 0 as first and 25 as last parameter to run all functions
#         functionNbr = i + 1
#         filenamebase = f"PSO_timeline_d{dimension}_f{functionNbr}"
#         titlebase = f"PSO on {function_dictionary[functionNbr][0]} with dimension {dimension}"
#
#         convergences = list()
#         final_results = list()
#         averages = list()
#
#         de.process_multiple_runs_pso(runs, functionNbr, function_dictionary, dimension, population_size,
#                                      bounds, 2000 * dimension, c1_pso, c2_pso, w_pso, convergences,
#                                      final_results, averages,
#                                      dirname, filenamebase, titlebase, "")

# dirname = "./output/SOMA_all-to-one/"
# for lt in long_times:
#     for i in lt:
#         functionNbr = i + 1
#         filenamebase = f"SOMA_all-to-one_timeline_d{dimension}_f{functionNbr}"
#         titlebase = f"SOMA all-to-one on {function_dictionary[functionNbr][0]} with dimension {dimension}"
#
#         convergences = list()
#         final_results = list()
#         averages = list()
#
#         de.process_multiple_runs_soma_all_to_one(runs, functionNbr, function_dictionary, dimension, population_size,
#                                                  bounds, 2000 * dimension, path_length_soma, step_size_soma, prt_soma,
#                                                  convergences,
#                                                  final_results, averages,
#                                                  dirname, filenamebase, titlebase, "")

# # SOMA all-to-all
# dirname = "./output/SOMA_all-to-all/"
# for lt in long_times:
#     for i in lt:
#         functionNbr = i + 1
#         filenamebase = f"SOMA_all-to-all_timeline_d{dimension}_f{functionNbr}"
#         titlebase = f"SOMA all-to-all on {function_dictionary[functionNbr][0]} with dimension {dimension}"
#
#         convergences = list()
#         final_results = list()
#         averages = list()
#
#         de.process_multiple_runs_soma_all_to_all(runs, functionNbr, function_dictionary, dimension, population_size,
#                                                  bounds, 2000 * dimension, path_length_soma, step_size_soma, prt_soma,
#                                                  convergences,
#                                                  final_results, averages,
#                                                  dirname, filenamebase, titlebase, "")

# SOMA all-to-one
# dirname = "./output/SOMA_all-to-one/"
# for i in range(0, 25):  # use 0 as first and 25 as last parameter to run all functions
#     functionNbr = i + 1
#     filenamebase = f"SOMA_all-to-one_timeline_d{dimension}_f{functionNbr}"
#     titlebase = f"SOMA all-to-one on {function_dictionary[functionNbr][0]} with dimension {dimension}"
#
#     convergences = list()
#     final_results = list()
#     averages = list()
#
#     de.process_multiple_runs_soma_all_to_one(runs, functionNbr, function_dictionary, dimension, population_size,
#                                              bounds, 2000 * dimension, path_length_soma, step_size_soma, prt_soma,
#                                              convergences,
#                                              final_results, averages,
#                                              dirname, filenamebase, titlebase, "")

# SOMA all-to-all
# dirname = "./output/SOMA_all-to-all/"
# for i in range(0, 25):  # use 0 as first and 25 as last parameter to run all functions
#     functionNbr = i + 1
#     filenamebase = f"SOMA_all-to-all_timeline_d{dimension}_f{functionNbr}"
#     titlebase = f"SOMA all-to-all on {function_dictionary[functionNbr][0]} with dimension {dimension}"
#
#     convergences = list()
#     final_results = list()
#     averages = list()
#
#     de.process_multiple_runs_soma_all_to_all(runs, functionNbr, function_dictionary, dimension, population_size,
#                                              bounds, 2000 * dimension, path_length_soma, step_size_soma, prt_soma,
#                                              convergences,
#                                              final_results, averages,
#                                              dirname, filenamebase, titlebase, "")

# # algorithms = ["DE_rand_1_bin", "DE_best_1_bin", "PSO", "SOMA_all-to-one", "SOMA_all-to-all"]
algorithms = ["PSO"]
for algorithm in algorithms:
    de.create_statistics_file(algorithm, 30)
