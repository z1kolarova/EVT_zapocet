import random
from enum import Enum
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import algorithms as al


def directory_preparation(dirname):
    Path(f"./{dirname}").mkdir(parents=True, exist_ok=True)


def write_solution_file(full_file_path, best_solution, fitness, timestamp_start, timestamp_end):
    file = open(full_file_path, "a")
    for value in best_solution:
        file.write(f"{value};")
    file.write(f"\nFitness;{fitness};")
    file.write(f"\nCalculations began;{timestamp_start};Calculations ended;{timestamp_end}\n")


def plot_and_save_single_line(dir_path, filename, title, x_label, y_label, y_values):
    x_points = range(1, len(y_values) + 1)
    y_points = np.asarray(y_values)
    plt.plot(x_points, y_points)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(f"{dir_path}/{filename}", bbox_inches='tight')
    plt.close()


def plot_and_save_many_lines(dir_path, filename, title, x_label, x_point_count, y_label, list_of_lists_with_y_values):
    x_points = range(1, x_point_count + 1)
    for result in list_of_lists_with_y_values:
        plt.plot(x_points, np.asarray(result))
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(f"./{dir_path}/{filename}", bbox_inches='tight')
    plt.close()


def plot_and_save_multiple_lines_with_legend(dir_path, filename, title, x_label, x_point_count, y_label,
                                             y_set_and_name_tuple_list):
    x_points = range(1, x_point_count + 1)
    for result in y_set_and_name_tuple_list:
        plt.plot(x_points, np.asarray(result[0]), label=result[1])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.savefig(f"./{dir_path}/{filename}", bbox_inches='tight')
    plt.close()


def process_multiple_runs_de_rand_1_bin(runs, cf_nbr, cf_dictionary, dimension, population_size, bounds, max_cf_evals,
                                        f, cr, convergences, final_results, averages,
                                        dirname, filenamebase, titlebase, statistics_filename):
    convergence_of_run = list()
    for i in range(runs):
        convergence_of_run = al.de_rand_1_bin(cf_nbr, cf_dictionary, dimension, population_size, bounds, max_cf_evals,
                                              f, cr)
        convergences.append(convergence_of_run)
        """de.save_plotted("./output/", f"{i}.png", titlebase, "Iterations", "CF Value", convergence_of_run)"""
        final_results.append(convergence_of_run[- 1])

    average_helper = list()
    for j in range(len(convergence_of_run)):
        average_helper.clear()
        for k in range(runs):
            average_helper.append(convergences[k][j])
        averages.append(np.average(average_helper))

    plot_and_save_single_line(dirname, f"{filenamebase}_average.png",
                              f"Average best solution timeline for\n{titlebase}",
                              "Generations", "CF Value", averages)
    plot_and_save_many_lines(dirname, f"{filenamebase}.png",
                             f"Evolution of CF Value for all solutions for\n{titlebase}",
                             "Generations", len(convergence_of_run), "CF Value", convergences)

    # """csv_data = Statistics(filenamebase, min(final_results), max(final_results),
    #                           np.mean(final_results),
    #                           np.median(final_results), np.std(final_results))
    #     statistics_csv(statistics_filename, csv_data)"""


def process_multiple_runs_de_best_1_bin(runs, cf_nbr, cf_dictrionary, dimension, population_size, bounds, max_cf_evals,
                                        f, cr, convergences, final_results, averages,
                                        dirname, filenamebase, titlebase, statistics_filename):
    convergence_of_run = list()
    for i in range(runs):
        convergence_of_run = al.de_best_1_bin(cf_nbr, cf_dictrionary, dimension, population_size, bounds, max_cf_evals,
                                              f, cr)
        convergences.append(convergence_of_run)
        # de.save_plotted("./output/de_best_1_bin/", f"{i}.png", titlebase, "Iterations", "CF Value",
        # convergence_of_run)
        final_results.append(convergence_of_run[- 1])

    average_helper = list()
    for j in range(len(convergence_of_run)):
        average_helper.clear()
        for k in range(runs):
            average_helper.append(convergences[k][j])
        averages.append(np.average(average_helper))

    plot_and_save_single_line(dirname, f"{filenamebase}_average.png",
                              f"Average best solution timeline for\n{titlebase}",
                              "Generations", "CF Value", averages)
    plot_and_save_many_lines(dirname, f"{filenamebase}.png",
                             f"Evolution of CF Value for all solutions for\n{titlebase}",
                             "Generations", len(convergence_of_run), "CF Value", convergences)

    # """csv_data = Statistics(filenamebase, min(final_results), max(final_results),
    #                           np.mean(final_results),
    #                           np.median(final_results), np.std(final_results))
    #     statistics_csv(statistics_filename, csv_data)"""


def process_multiple_runs_pso(runs, cf_nbr, cf_dictrionary, dimension, population_size, bounds, max_cf_evals,
                              c1, c2, w, convergences, final_results, averages,
                              dirname, filenamebase, titlebase, statistics_filename):
    convergence_of_run = list()
    for i in range(runs):
        convergence_of_run = al.pso(cf_nbr, cf_dictrionary, dimension, population_size, bounds, max_cf_evals,
                                    c1, c2, w)
    #     convergences.append(convergence_of_run)
    #     # de.save_plotted("./output/de_best_1_bin/", f"{i}.png", titlebase, "Iterations", "CF Value",
    #     # convergence_of_run)
    #     final_results.append(convergence_of_run[- 1])
    #
    # average_helper = list()
    # for j in range(len(convergence_of_run)):
    #     average_helper.clear()
    #     for k in range(runs):
    #         average_helper.append(convergences[k][j])
    #     averages.append(np.average(average_helper))
    #
    # plot_and_save_single_line(dirname, f"{filenamebase}_average.png",
    #                           f"Average best solution timeline for\n{titlebase}",
    #                           "Generations", "CF Value", averages)
    # plot_and_save_many_lines(dirname, f"{filenamebase}.png",
    #                          f"Evolution of CF Value for all solutions for\n{titlebase}",
    #                          "Generations", len(convergence_of_run), "CF Value", convergences)


def process_multiple_runs_soma_all_to_one(runs, cf_nbr, cf_dictrionary, dimension, population_size, bounds,
                                          max_cf_evals, path_length, step_size, prt,
                                          convergences, final_results, averages,
                                          dirname, filenamebase, titlebase, statistics_filename):
    convergence_of_run = list()
    for i in range(runs):
        # convergence_of_run = (
        al.soma_all_to_one(cf_nbr, cf_dictrionary, dimension, population_size, bounds,
                           max_cf_evals, path_length, step_size, prt)
        # )
        # convergences.append(convergence_of_run)
        # de.save_plotted("./output/de_best_1_bin/", f"{i}.png", titlebase, "Iterations", "CF Value",
        # convergence_of_run)
    #     final_results.append(convergence_of_run[- 1])
    #
    # average_helper = list()
    # for j in range(len(convergence_of_run)):
    #     average_helper.clear()
    #     for k in range(runs):
    #         average_helper.append(convergences[k][j])
    #     averages.append(np.average(average_helper))
    #
    # plot_and_save_single_line(dirname, f"{filenamebase}_average.png",
    #                           f"Average best solution timeline for\n{titlebase}",
    #                           "Migrations", "CF Value", averages)
    # plot_and_save_many_lines(dirname, f"{filenamebase}.png",
    #                          f"Evolution of CF Value for all solutions for\n{titlebase}",
    #                          "Migrations", len(convergence_of_run), "CF Value", convergences)


def process_multiple_runs_soma_all_to_all(runs, cf_nbr, cf_dictrionary, dimension, population_size, bounds,
                                          max_cf_evals, path_length, step_size, prt,
                                          convergences, final_results, averages,
                                          dirname, filenamebase, titlebase, statistics_filename):
    convergence_of_run = list()
    for i in range(runs):
        # convergence_of_run = (
        al.soma_all_to_all(cf_nbr, cf_dictrionary, dimension, population_size, bounds,
                           max_cf_evals, path_length, step_size, prt)
        # )
        # convergences.append(convergence_of_run)
        # de.save_plotted("./output/de_best_1_bin/", f"{i}.png", titlebase, "Iterations", "CF Value",
        # convergence_of_run)
        # final_results.append(convergence_of_run[- 1])

    # average_helper = list()
    # for j in range(len(convergence_of_run)):
    #     average_helper.clear()
    #     for k in range(runs):
    #         average_helper.append(convergences[k][j])
    #     averages.append(np.average(average_helper))
    #
    # plot_and_save_single_line(dirname, f"{filenamebase}_average.png",
    #                           f"Average best solution timeline for\n{titlebase}",
    #                           "Migrations", "CF Value", averages)
    # plot_and_save_many_lines(dirname, f"{filenamebase}.png",
    #                          f"Evolution of CF Value for all solutions for\n{titlebase}",
    #                          "Migrations", len(convergence_of_run), "CF Value", convergences)


def create_statistics_file(algorithm_name, dimension):
    output_file = f"./output/{algorithm_name}_d{dimension}.csv"
    statistics_file = open(output_file, "a")
    for i in range(1, 26):
        runs_file = f"./output/{algorithm_name}/{algorithm_name}_d{dimension}_f{i}.csv"
        statistics_file.write(f"f{i};")
        with open(runs_file) as rf:
            for line in rf:
                if line.startswith("Fitness"):
                    fitness = line.split(';')[1].replace(".", ",")
                    statistics_file.write(f"{fitness};")
        statistics_file.write(f"\n")