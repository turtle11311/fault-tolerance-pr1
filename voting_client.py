from __future__ import print_function
import logging
import grpc
import voting_pb2
import voting_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
import time

def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = voting_pb2_grpc.eVotingStub(channel)

        # PreAuth
        response = stub.PreAuth(voting_pb2.VoterName(name='Client'))
        if response.value == b'00001':
            print("PreAuth successful")
        else:
            print("PreAuth failed")

        # Auth
        response = stub.Auth(voting_pb2.AuthRequest(name=voting_pb2.VoterName(name='Client'), response=voting_pb2.Response(value=b'01234')))
        if response.value == b'00010':
            print("Auth successful")
        else:
            print("Auth failed")

        # CreateElection
        now = time.time() # Compute Timestamp from current time
        seconds = int(now)
        nanos = int((now - seconds) * 10**9)
        timestamp = Timestamp(seconds=seconds, nanos=nanos)
        response = stub.CreateElection(voting_pb2.Election(name='Client',groups="Group1",choices="Number1",end_date= timestamp,token=voting_pb2.AuthToken(value=b'01234')))
        if response.code == 1:
            print("CreateElection successful")
        else:
            print("CreateElection failed")

        # CastVote
        response = stub.CastVote(voting_pb2.Vote(election_name='Election1',choice_name='Choice2',token=voting_pb2.AuthToken(value=b'01234')))
        if response.code == 2:
            print("CastVote successful")
        else:
            print("CastVote failed")

         # GetResult
        response = stub.GetResult(voting_pb2.ElectionName(name='Election1'))
        if (response.status == 1) and (response.count[0].choice_name == 'Choice1') and (response.count[0].count == 1) and (response.count[0].token.value == b'abcd'):
            print("GetResult successful")
        else:
            print("GetResult failed")


if __name__ == '__main__':
    logging.basicConfig()
    run()
