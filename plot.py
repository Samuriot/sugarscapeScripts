# Plots 1 json file for population, disease deaths, and percentage sick all over timesteps.

import json
import sys
import glob
import matplotlib.pyplot as plt

def load_json (filename):
    with open(filename, 'r') as file:
        try:
            return json.load(file)
        except:
            print("error loading json... quitting program.")
            sys.exit()

def load_data (json_data):
    timesteps = [entry["timestep"] for entry in json_data]
    population = [entry["population"] for entry in json_data]
    agent_disease_deaths = [entry["agentDiseaseDeaths"] for entry in json_data]
    sick_agents = [entry["sickAgentsPercentage"] for entry in json_data]
    return timesteps, population, agent_disease_deaths, sick_agents

def plot_population (timesteps, population, filename):
    plt.plot(timesteps, population, linestyle='-', label='Population', color="blue")
    plt.xlabel('Timestep')
    plt.ylabel('Population')
    plt.title('Population over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{filename}_population.png")
    plt.cla()

def plot_disease_deaths (timesteps, agent_deaths, filename):
    plt.plot(timesteps, agent_deaths, linestyle='-', label='Population', color="red")
    plt.xlabel('Timestep')
    plt.ylabel('Deaths')
    plt.title('Deaths over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{filename}_disease_deaths.png")
    plt.cla()

def plot_incidence (timesteps, incidence, filename):
    plt.plot(timesteps, incidence, linestyle='-', label='Population', color="green")
    plt.xlabel('Timestep')
    plt.ylabel('Sick (%)')
    plt.title('Sick Percentage over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{filename}_sick_percentage.png")
    plt.cla()

if __name__ == "__main__":
    filename = sys.argv[1]
    json = load_json(filename)
    timesteps, population, agent_deaths, sick_agents = load_data(json)
    plot_population(timesteps, population, filename) 
    plot_disease_deaths(timesteps, agent_deaths, filename)
    plot_incidence(timesteps, sick_agents, filename)