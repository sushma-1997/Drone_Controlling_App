import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Plane Controller',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Plane Controller'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _throttle = 0;
  int _elevatorPitch = 0;

  Future<void> _setThrottle(int percentage) async {
    final response =
        await http.post(Uri.parse('http://localhost:5000/throttle'),
            headers: <String, String>{
              'Content-Type': 'application/json; charset=UTF-8',
            },
            body: jsonEncode(<String, int>{'throttle_percentage': percentage}));

    if (response.statusCode == 200) {
      setState(() {
        _throttle = percentage;
      });
    } else {
      print('Failed to set throttle. Error code: ${response.statusCode}');
    }
  }

  Future<void> _setElevatorPitch(int percentage) async {
    final response =
        await http.post(Uri.parse('http://localhost:5000/elevator_pitch'),
       
            headers: <String, String>{
              'Content-Type': 'application/json; charset=UTF-8',
            },
            body: jsonEncode(<String, int>{'elevator_pitch_percentage': percentage}));

    if (response.statusCode == 200) {
      setState(() {
        _elevatorPitch = percentage;
      });
    } else {
      print(
          'Failed to set elevator/pitch. Error code: ${response.statusCode}');
    }
  }
void _armVehicle() async {
    try {
      final response = await http.get(Uri.parse('http://localhost:5000/arm'));
      if (response.statusCode == 200) {
        print('ARM command sent successfully!');
      } else {
        print('Failed to send ARM command. Error code: ${response.statusCode}');
      }
    } catch (error) {
      print('Failed to send ARM command. Error: $error');
    }
  }

  void _disarmVehicle() async {
    try {
      final response = await http.get(Uri.parse('http://localhost:5000/disarm'));
      if (response.statusCode == 200) {
        print('DISARM command sent successfully!');
      } else {
        print('Failed to send DISARM command. Error code: ${response.statusCode}');
      }
    } catch (error) {
      print('Failed to send DISARM command. Error: $error');
    }
  }


@override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: _armVehicle,
              child: Text(
                'ARM',
                style: TextStyle(fontSize: 20),
              ),
              style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all<Color>(Colors.white),
                padding: MaterialStateProperty.all<EdgeInsets>(EdgeInsets.all(20)),
                minimumSize: MaterialStateProperty.all<Size>(Size(200, 0)),
                shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                  RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
                foregroundColor: MaterialStateProperty.all<Color>(Colors.blue),
              ),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _disarmVehicle,
              child: Text(
                'DISARM',
                style: TextStyle(fontSize: 20),
              ),
              style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all<Color>(Colors.white),
                padding: MaterialStateProperty.all<EdgeInsets>(EdgeInsets.all(20)),
                minimumSize: MaterialStateProperty.all<Size>(Size(200, 0)),
                shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                  RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
                foregroundColor: MaterialStateProperty.all<Color>(Colors.red),
              ),
            ),
            SizedBox(height: 30),
            Text(
              'Throttle: $_throttle%',
              style: Theme.of(context).textTheme.headline5,
            ),
            SizedBox(height: 30),
            Text(
              'Elevator/Pitch: $_elevatorPitch%',
              style: Theme.of(context).textTheme.headline5,
            ),
            SizedBox(height: 30),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text('Throttle'),
                    SizedBox(height: 20),
                    IconButton(
                        icon: Icon(Icons.arrow_upward),
                        onPressed: () async {
                          if (_throttle < 100) {
                            await _setThrottle(_throttle + 1);
                          }
                        }),
                    SizedBox(height: 20),
                    Text('$_throttle%'),
                    SizedBox(height: 20),
                    IconButton(
                        icon: Icon(Icons.arrow_downward),
                        onPressed: () async {
                          if (_throttle > 0) {
                            await _setThrottle(_throttle - 1);
                          }
                        }),
                  ],
                ),
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text('Elevator/Pitch'),
                    SizedBox(height: 20),
                    IconButton(
                        icon: Icon(Icons.arrow_upward),
                        onPressed: () async {
                          if (_elevatorPitch < 100) {
                            await _setElevatorPitch(_elevatorPitch + 1);
                          }
                        }),
                    SizedBox(height: 20),
                    Text('$_elevatorPitch%'),
                    SizedBox(height: 20),
                    IconButton(
                        icon: Icon(Icons.arrow_downward),
                        onPressed: () async {
                          if (_elevatorPitch > -100) {
                            await _setElevatorPitch(_elevatorPitch - 1);
                          }
                        }),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }


}
