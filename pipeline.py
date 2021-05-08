from dagster import pipeline, repository
import sys
sys.path.append('./solids')
import wm

@pipeline
def load():
    wm.load()

@repository
def wine_facts_repository():
    return [load]