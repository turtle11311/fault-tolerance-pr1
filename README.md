# Online Electronic Voting – Part I. RPC Interface

## How to run server
```shell
python voting_server.py
```

## How to run client
```shell
python voting_client.py
```

## The Design
The client calls the gRPC stub method, which sends a proto request to the server, and then the client checks if the response value is correct.
![design diagram](https://user-images.githubusercontent.com/1523131/159169464-dc38590d-8090-4ffe-a93f-709d40c6a6b4.png)

## Implemtentation
We chose python as the programming language for this project.

The gRPC tool generates the basic servicer class from the project proto file and we need to implement the derived classes of the basic servicer.
![Servicer UML](https://user-images.githubusercontent.com/1523131/159171363-d56f3c0e-7300-451c-ad2c-fcd78f4f8302.png)

The client just calls the gRPC stub directly.

## Evaluation

The client just calls the gRPC stub directly, and then the client checks if the response value is expected value.

```python
# PreAuth
        response = stub.PreAuth(voting_pb2.VoterName(name='Client'))
        if response.value == b'00001':
            print("PreAuth successful")
        else:
            print("PreAuth failed")
```
