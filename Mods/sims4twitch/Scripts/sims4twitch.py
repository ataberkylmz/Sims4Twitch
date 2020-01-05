import sims4.commands
import sims4
import services
import sims4.reload as r
import os.path
from objects import ALL_HIDDEN_REASONS, HiddenReasonFlag
from protocolbuffers import Consts_pb2, DistributorOps_pb2, SimObjectAttributes_pb2
import testClient

#TODO: Use streamlabs' Socket API to get bits, donations, etc and implement the rest.
#TODO: Find a way to use requests module in Sims 4.
#TODO: DO NOT PUT THE TEST SERVER INTO MODS FOLDER AS IT CONTAINS INFINITE LOOP!!!!!!!

@sims4.commands.Command('reload', command_type=sims4.commands.CommandType.Live)
def reload(module: str, _connection=None):
    output = sims4.commands.CheatOutput(_connection)
    try:
        dirname = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(dirname, module) + ".py"
        output("Reloading {}".format(filename))
        reloaded_module = r.reload_file(filename)
        if reloaded_module is not None:
            output("Done reloading!")
        else:
            output("Error loading module or module does not exist")
    except BaseException as e:
        output("Reload failed: ")
        for v in e.args:
            output(v)


@sims4.commands.Command('test', command_type=sims4.commands.CommandType.Live)
def test(_connection=None):
    output = sims4.commands.CheatOutput(_connection)

    current_sim = services.active_sim_info()
    household = services.household_manager().get(current_sim.household.id)

    output("selected sim id: {}".format(current_sim.sim_id))
    output("current hosuehold id: {}".format(current_sim.household))
    current_sim.household.funds.add(500, Consts_pb2.TELEMETRY_SIM_WALLET_FUNDED, current_sim.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS))
    '''for sim_info in services.sim_info_manager().objects:
        output("sim id: {}".format(sim_info.sim_id))
        output("sim last name: {}".format(sim_info.last_name))
    '''

@sims4.commands.Command('sockettest', command_type=sims4.commands.CommandType.Live)
def socket_test(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    _client = testClient.Client()
    _client.connect(output)
    _client.send()
    received = _client.listen()
    output("Data received: {}".format(received))
    

