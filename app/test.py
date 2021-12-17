import os

from app.hybrid_program_generation.hybrid_program_generator import create_hybrid_program

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")
templatesDirectory = os.path.join(basedir, 'files')
beforeLoop = 'a123,b456'
afterLoop = 'null'
loopCondition = 'test'
taskIdProgramMap = {'a123': os.path.join(templatesDirectory, 'QSVMExecutorService.py'),
                    'b456': os.path.join(templatesDirectory, 'QSVMOptimizerService.py')}
programs = create_hybrid_program(beforeLoop, afterLoop, loopCondition, taskIdProgramMap)

if 'error' in programs:
    print(programs['error'])