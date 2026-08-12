import 'package:flutter/material.dart';
import 'package:reffin_cards/reffin_cards.dart';

void main() => runApp(const CardReferenceExample());

class CardReferenceExample extends StatelessWidget {
  const CardReferenceExample({super.key});

  @override
  Widget build(BuildContext context) {
    final network = CardNetwork.tryParse('visa') ?? CardNetwork.unknown;
    final funding = FundingType.tryParse('credit') ?? FundingType.unknown;
    final outcome = PaymentOutcome.tryParse('approved') ?? PaymentOutcome.unknown;

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Reffin card reference data')),
        body: ListView(
          children: <Widget>[
            ListTile(
              leading: Icon(network.icon),
              title: Text(network.label),
              subtitle: Text('Normalized ID: ${network.id}'),
            ),
            ListTile(
              leading: Icon(funding.icon),
              title: Text(funding.label),
              subtitle: Text(funding.description),
            ),
            ListTile(
              leading: Icon(outcome.icon),
              title: Text(outcome.label),
              subtitle: Text(outcome.description),
            ),
          ],
        ),
      ),
    );
  }
}
