import datetime

import math
import random

import numpy as np

import functions as fc
import dataexports as de


def create_initial_population(dimension, population_size, bounds):
    population = bounds[0] + (np.random.rand(population_size, dimension) * (bounds[1] - bounds[0]))
    return population


def ensure_value_within_bounds_reflection(value, bounds):
    while value < bounds[0] or value > bounds[1]:
        if value < bounds[0]:
            value = bounds[0] + (bounds[0] - value)
        elif value > bounds[1]:
            value = bounds[1] + (bounds[1] - value)
    return value


def de_rand_1_bin(cf_nbr, cf_dictionary, dimension, population_size, bounds, max_cf_evals,
                  scaling_factor_f, crossover_probability_cr):
    population = create_initial_population(dimension, population_size, bounds)
    fitnesses = list()
    convergence_list = list()
    start_timestamp = datetime.datetime.now()
    for individual in population:
        fitnesses.append(cf_dictionary[cf_nbr][1](individual))
    best_fitness_index = np.argmin(fitnesses)
    cf_eval_counter = population_size

    while (cf_eval_counter + population_size) < max_cf_evals:
        for i in range(population_size):
            r1, r2, r3 = np.random.choice(population_size, 3, False)
            mutation_vector = population[r1] + (scaling_factor_f * (population[r2] - population[r3]))

            crossover_mask = np.random.rand(dimension) < crossover_probability_cr
            offspring = np.where(crossover_mask, mutation_vector, population[i])

            for j in range(dimension):
                offspring[j] = ensure_value_within_bounds_reflection(offspring[j], bounds)

            offspring_fitness = cf_dictionary[cf_nbr][1](offspring)
            cf_eval_counter += 1

            if offspring_fitness < fitnesses[i]:
                population[i] = offspring
                fitnesses[i] = offspring_fitness
        best_fitness_index = np.argmin(fitnesses)
        convergence_list.append(fitnesses[best_fitness_index])

    end_timestamp = datetime.datetime.now()
    de.write_solution_file(f"./output/DE_rand_1_bin/DE_rand_1_bin_d{dimension}_f{cf_nbr}.csv",
                           population[best_fitness_index], convergence_list[-1], start_timestamp, end_timestamp)
    return convergence_list


def de_best_1_bin(cf_nbr, cf_dictionary, dimension, population_size, bounds, max_cf_evals,
                  scaling_factor_f, crossover_probability_cr):
    population = create_initial_population(dimension, population_size, bounds)
    fitnesses = list()
    convergence_list = list()
    start_timestamp = datetime.datetime.now()
    for individual in population:
        fitnesses.append(cf_dictionary[cf_nbr][1](individual))
    best_fitness_index = np.argmin(fitnesses)
    cf_eval_counter = population_size

    while (cf_eval_counter + population_size) < max_cf_evals:
        for i in range(population_size):
            r1, r2 = np.random.choice(population_size, 2, False)
            mutation_vector = population[best_fitness_index] + scaling_factor_f * (population[r1] - population[r2])

            crossover_mask = np.random.rand(dimension) < crossover_probability_cr
            offspring = np.where(crossover_mask, mutation_vector, population[i])

            for j in range(dimension):
                offspring[j] = ensure_value_within_bounds_reflection(offspring[j], bounds)

            offspring_fitness = cf_dictionary[cf_nbr][1](offspring)
            cf_eval_counter += 1

            if offspring_fitness < fitnesses[i]:
                population[i] = offspring
                fitnesses[i] = offspring_fitness
        best_fitness_index = np.argmin(fitnesses)
        convergence_list.append(fitnesses[best_fitness_index])

    end_timestamp = datetime.datetime.now()
    de.write_solution_file(f"./output/DE_best_1_bin/DE_best_1_bin_d{dimension}_f{cf_nbr}.csv",
                           population[best_fitness_index], convergence_list[-1], start_timestamp, end_timestamp)
    return convergence_list


def pso(cf_nbr, cf_dictionary, dimension, population_size, bounds, max_cf_evals, c1, c2, w):
    population = create_initial_population(dimension, population_size, bounds)
    fitnesses = np.array([cf_dictionary[cf_nbr][1](individual) for individual in population])
    pbests = population.copy()
    pbest_fitnesses = fitnesses.copy()
    starting_inertia = np.zeros(dimension)
    inertias = np.tile(starting_inertia, (population_size, 1))
    convergence_list = []
    start_timestamp = datetime.datetime.now()

    best_fitness_index = np.argmin(fitnesses)
    gbest = population[best_fitness_index].copy()
    gbest_fitness = fitnesses[best_fitness_index]
    cf_eval_counter = population_size

    while (cf_eval_counter + population_size) < max_cf_evals:
        for i in range(population_size):
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)

            vt1 = w * inertias[i] + (c1 * r1 * (pbests[i][0] - population[i]) + (c2 * r2 * (gbest - population[i])))
            inertias[i] = vt1
            population[i] = population[i] + vt1

            for j in range(dimension):
                population[i][j] = ensure_value_within_bounds_reflection(population[i][j], bounds)
            new_fitness = cf_dictionary[cf_nbr][1](population[i])
            cf_eval_counter += 1
            if new_fitness < pbest_fitnesses[i]:
                pbests[i] = population[i]
                pbest_fitnesses[i] = new_fitness
            fitnesses[i] = new_fitness

        best_new_fitness_index = np.argmin(fitnesses)
        if fitnesses[best_new_fitness_index] < gbest_fitness:
            best_fitness_index = best_new_fitness_index
            gbest = population[best_fitness_index]
            gbest_fitness = fitnesses[best_fitness_index]
        convergence_list.append(gbest_fitness)

    end_timestamp = datetime.datetime.now()
    de.write_solution_file(f"./output/PSO/PSO_d{dimension}_f{cf_nbr}.csv",
                           population[best_fitness_index], convergence_list[-1], start_timestamp, end_timestamp)
    return convergence_list


def soma_all_to_one(cf_nbr, cf_dictionary, dimension, population_size, bounds, max_cf_evals, path_length, step_size,
                    prt):
    migrations_total = (max_cf_evals * step_size) / (path_length * (population_size - 1))
    population = create_initial_population(dimension, population_size, bounds)
    fitnesses = np.array([cf_dictionary[cf_nbr][1](individual) for individual in population])

    convergence_list = []
    start_timestamp = datetime.datetime.now()

    best_fitness_index = np.argmin(fitnesses)  # leader
    leader = population[best_fitness_index]

    for m in range(int(migrations_total)):

        for i in range(population_size):
            t = 0
            while t < path_length:
                movement = leader - population[i]
                prts = np.random.rand(dimension)
                prt_vector = np.array(prts < prt, dtype=int)
                step_individual = population[i] + movement * t * prt_vector
                step_fitness = cf_dictionary[cf_nbr][1](step_individual)

                if step_fitness < fitnesses[i]:
                    population[i] = step_individual
                    fitnesses[i] = step_fitness

                t += step_size
        best_fitness_index = np.argmin(fitnesses)  # leader
        leader = population[best_fitness_index]
        convergence_list.append(fitnesses[best_fitness_index])

    end_timestamp = datetime.datetime.now()
    de.write_solution_file(f"./output/SOMA_all-to-one/SOMA_all-to-one_d{dimension}_f{cf_nbr}.csv",
                           population[best_fitness_index], convergence_list[-1], start_timestamp, end_timestamp)
    return convergence_list


def soma_all_to_all(cf_nbr, cf_dictionary, dimension, population_size, bounds, max_cf_evals, path_length, step_size,
                    prt):
    migrations_total = (max_cf_evals * step_size) / (path_length * population_size * (population_size - 1))
    population = create_initial_population(dimension, population_size, bounds)
    fitnesses = np.array([cf_dictionary[cf_nbr][1](individual) for individual in population])

    best_fitness_index = np.argmin(fitnesses)

    convergence_list = []
    start_timestamp = datetime.datetime.now()

    post_migration_positions = population.copy()
    post_migration_fitnesses = fitnesses.copy()

    for m in range(int(migrations_total)):

        for i in range(population_size):
            for g in range(population_size):
                t = 0
                while t < path_length:
                    movement = population[g] - population[i]
                    prts = np.random.rand(dimension)
                    prt_vector = np.array(prts < prt, dtype=int)
                    step_individual = population[i] + movement * t * prt_vector
                    step_fitness = cf_dictionary[cf_nbr][1](step_individual)

                    if step_fitness < post_migration_fitnesses[i]:
                        post_migration_positions[i] = step_individual
                        post_migration_fitnesses[i] = step_fitness

                    t += step_size

        for i in range(population_size):
            if post_migration_fitnesses[i] < fitnesses[i]:
                population[i] = post_migration_positions[i]

        best_fitness_index = np.argmin(fitnesses)
        convergence_list.append(fitnesses[best_fitness_index])

    end_timestamp = datetime.datetime.now()
    de.write_solution_file(f"./output/SOMA_all-to-all/SOMA_all-to-all_d{dimension}_f{cf_nbr}.csv",
                           population[best_fitness_index], convergence_list[-1], start_timestamp, end_timestamp)
    return convergence_list
