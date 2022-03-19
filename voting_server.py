from concurrent import futures
import logging

import grpc
import voting_pb2
import voting_pb2_grpc

class Voting(voting_pb2_grpc.eVotingServicer):

    def PreAuth(self, request, context):
        return voting_pb2.Challenge(value=b'00001')
    def Auth(self, request, context):
        return voting_pb2.AuthToken(value=b'00010')
    def CreateElection(self, request, context):
        return voting_pb2.ElectionStatus(code=1)
    def CastVote(self, request, context):
        return voting_pb2.VoteStatus(code=2)
    def GetResult(self, request, context):
        return voting_pb2.ElectionResult(status=1,count=[voting_pb2.VoteCount(choice_name='Choice1', count=1, token=voting_pb2.AuthToken(value=b'abcd'))])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    voting_pb2_grpc.add_eVotingServicer_to_server(Voting(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
