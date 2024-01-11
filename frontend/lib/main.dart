import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:io';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_tts/flutter_tts.dart';

void main() {
  runApp(
    MaterialApp(
      localizationsDelegates: [
        /*MaterialLocalizations.delegate,*/
        GlobalWidgetsLocalizations.delegate,
      ],
      home: MyApp(),
    ),
  );
}

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String RESULT = "";
  FlutterTts flutterTts = FlutterTts();
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
      appBar: AppBar(
        title: Text("My App"),
      ),
      body: Center(
          child: Column(mainAxisSize: MainAxisSize.max, children: [
        SizedBox(
            width: 200,
            height: 50,
            child: ElevatedButton(
              onPressed: () {
                predict();
              },
              child: Text("Press"),
              style: ButtonStyle(
                  shape: MaterialStateProperty.all(RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(15),
                  )),
                  backgroundColor:
                      MaterialStateProperty.all<Color>(Colors.green)),
            )),
        SizedBox(
          height: 16,
        )
      ])),
    ));
  }

  Future predict() async {
    showDialog(
      context: this.context,
      builder: (context) {
        return const Center(child: CircularProgressIndicator());
      },
    );
    http.Response res =
        await http.get(Uri.parse("https://6589-49-204-11-90.in.ngrok.io"));
    var next = res.body;
    var decoded = jsonDecode(next);
    //return Text(decoded["output"]);
    Navigator.of(this.context).pop();
    setState(() {
      RESULT = decoded["output"];
    });
    await flutterTts.speak(RESULT);
  }
}
