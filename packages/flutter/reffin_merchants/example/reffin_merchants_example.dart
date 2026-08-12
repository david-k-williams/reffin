import 'package:flutter/material.dart';
import 'package:reffin_merchants/reffin_merchants.dart';

void main() => runApp(const MerchantExampleApp());

class MerchantExampleApp extends StatelessWidget {
  const MerchantExampleApp({super.key});

  @override
  Widget build(BuildContext context) {
    final restaurant = resolveMcc('5812', MccVendor.visa);

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Merchant category lookup')),
        body: Center(
          child: restaurant == null
              ? const Text('MCC not found')
              : ListTile(
                  leading: Icon(restaurant.icon),
                  title: Text(restaurant.name),
                  subtitle: Text(
                    '${restaurant.mcc?.code} · ${restaurant.group.label}',
                  ),
                ),
        ),
      ),
    );
  }
}
